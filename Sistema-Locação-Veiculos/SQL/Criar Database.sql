-- Criação do banco de dados
CREATE DATABASE sistema_locacao_veiculos;
USE sistema_locacao_veiculos;

-- Tabela de login de Usuários
CREATE TABLE UsuáriosLogin (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
senha_hash VARCHAR(255) NOT NULL
);

-- Tabela de Usuários
CREATE TABLE Usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    ativo INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    endereco TEXT
);

-- Tabela da Categoria dos Veículos
CREATE TABLE VeiculoCategoria (
	categoria_id INT AUTO_INCREMENT PRIMARY KEY,
	fabricante VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    ano INT NOT NULL
);


-- Tabela de Veículos
CREATE TABLE Veiculos (
    veiculo_id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT,
    ativo INT NOT NULL,
    placa VARCHAR(20) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES VeiculoCategoria(categoria_id) ON DELETE CASCADE
);

-- Tabela de Localizações
CREATE TABLE Localizacao (
    localizacao_id INT AUTO_INCREMENT PRIMARY KEY,
    endereco TEXT NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    cep VARCHAR(20) NOT NULL
);

-- Tabela de Locações
CREATE TABLE Locacoes (
    locacao_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    veiculo_id INT,
    localizacao_id INT,
    ativo INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    preco_total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(veiculo_id) ON DELETE CASCADE,
    FOREIGN KEY (localizacao_id) REFERENCES Localizacao(localizacao_id) ON DELETE CASCADE
);

-- Tabela de Pagamentos
CREATE TABLE Pagamentos (
    pagamento_id INT AUTO_INCREMENT PRIMARY KEY,
    locacao_id INT,
    data_pagamento DATE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    metodo_pagamento VARCHAR(50) NOT NULL,
    FOREIGN KEY (locacao_id) REFERENCES Locacoes(locacao_id) ON DELETE CASCADE
);

-- Tabela de Manutenção de Veículos
CREATE TABLE ManutencaoVeiculos (
    manutencao_id INT AUTO_INCREMENT PRIMARY KEY,
    veiculo_id INT,
    data_manutencao DATE NOT NULL,
    descricao TEXT NOT NULL,
    custo DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(veiculo_id) ON DELETE CASCADE
);

-- Tabela de Avaliações de Usuários
CREATE TABLE AvaliacoesUsuarios (
    avaliacao_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    veiculo_id INT,
    data_avaliacao DATE NOT NULL,
    nota INT CHECK (nota BETWEEN 1 AND 5),
    comentario TEXT,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(veiculo_id) ON DELETE CASCADE
);

-- Tabela de Reservas
CREATE TABLE Reservas (
    reserva_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    veiculo_id INT,
    data_reserva DATE NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(veiculo_id) ON DELETE CASCADE
);

-- Tabela de Histórico de Preços
CREATE TABLE HistoricoPrecos (
    preco_id INT AUTO_INCREMENT PRIMARY KEY,
    veiculo_id INT,
    data_efetiva DATE NOT NULL,
    tarifa_diaria DECIMAL(10, 2) NOT NULL,
    tarifa_semanal DECIMAL(10, 2),
    tarifa_mensal DECIMAL(10, 2),
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(veiculo_id) ON DELETE CASCADE
);
