-- Inserindo dados na tabela Usuarios
INSERT INTO Usuarios (ativo,nome, email, senha, telefone, endereco) VALUES
(1,'João da Silva', 'joao.silva@email.com', 'senha123', '11987654321', 'Rua A, 123, São Paulo, SP'),
(1,'Maria Oliveira', 'maria.oliveira@email.com', 'senha456', '11987654322', 'Rua B, 456, Rio de Janeiro, RJ'),
(1,'Carlos Souza', 'carlos.souza@email.com', 'senha789', '11987654323', 'Rua C, 789, Belo Horizonte, MG'),
(1,'Ana Costa', 'ana.costa@email.com', 'senha101', '11987654324', 'Rua D, 123, Porto Alegre, RS'),
(1,'Pedro Lima', 'pedro.lima@email.com', 'senha202', '11987654325', 'Rua E, 456, Curitiba, PR');

-- Inserindo dados na tabela VeiculoCategoria
INSERT INTO VeiculoCategoria (fabricante, modelo, ano) VALUES
('Toyota', 'Corolla', 2020),
('Honda', 'Civic', 2019),
('Ford', 'Fiesta', 2018),
('Chevrolet', 'Onix', 2021),
('Volkswagen', 'Golf', 2020);

-- Inserindo dados na tabela Veiculos
INSERT INTO Veiculos (categoria_id, ativo, placa, status) VALUES
(1, 1,'ABC-1234', 'Disponível'),
(2, 1,'DEF-5678', 'Em manutenção'),
(3, 1,'GHI-9101', 'Locado'),
(4, 1,'JKL-1122', 'Disponível'),
(5, 1,'MNO-3344', 'Locado');

-- Inserindo dados na tabela Localizacao
INSERT INTO Localizacao (endereco, cidade, estado, cep) VALUES
('Avenida Paulista, 1000', 'São Paulo', 'SP', '01310-100'),
('Praia de Copacabana, 500', 'Rio de Janeiro', 'RJ', '22070-010'),
('Praça da Liberdade, 300', 'Belo Horizonte', 'MG', '30140-010'),
('Rua da Praia, 200', 'Porto Alegre', 'RS', '90010-000'),
('Avenida das Torres, 700', 'Curitiba', 'PR', '80040-010');

-- Inserindo dados na tabela Locacoes
INSERT INTO Locacoes (usuario_id, veiculo_id, localizacao_id, ativo, data_inicio, data_fim, preco_total, status) VALUES
(1, 1, 1, 1, '2024-05-01', '2024-05-10', 500.00, 'Concluída'),
(2, 3, 2, 1,'2024-05-05', '2024-05-15', 800.00, 'Ativa'),
(3, 2, 3, 1,'2024-06-01', '2024-06-10', 600.00, 'Reservada'),
(4, 4, 4, 1,'2024-05-10', '2024-05-20', 700.00, 'Ativa'),
(5, 5, 5, 1,'2024-05-15', '2024-05-25', 900.00, 'Concluída');

-- Inserindo dados na tabela Pagamentos
INSERT INTO Pagamentos (locacao_id, data_pagamento, valor, metodo_pagamento) VALUES
(1, '2024-05-01', 500.00, 'Cartão de Crédito'),
(2, '2024-05-05', 800.00, 'Boleto Bancário'),
(3, '2024-06-01', 600.00, 'Cartão de Débito'),
(4, '2024-05-10', 700.00, 'Transferência Bancária'),
(5, '2024-05-15', 900.00, 'Pix');

-- Inserindo dados na tabela ManutencaoVeiculos
INSERT INTO ManutencaoVeiculos (veiculo_id, data_manutencao, descricao, custo) VALUES
(2, '2024-05-01', 'Troca de óleo e filtros', 150.00),
(1, '2024-04-15', 'Revisão geral', 300.00),
(3, '2024-05-20', 'Troca de pneus', 400.00),
(4, '2024-05-25', 'Alinhamento e balanceamento', 200.00),
(5, '2024-06-05', 'Troca de bateria', 250.00);

-- Inserindo dados na tabela AvaliacoesUsuarios
INSERT INTO AvaliacoesUsuarios (usuario_id, veiculo_id, data_avaliacao, nota, comentario) VALUES
(1, 1, '2024-05-11', 5, 'Excelente carro, muito confortável.'),
(2, 3, '2024-05-16', 4, 'Veículo em boas condições, mas precisa de pequenos reparos.'),
(3, 2, '2024-06-11', 3, 'Carro razoável, mas poderia ser melhor mantido.'),
(4, 4, '2024-05-21', 5, 'Ótimo serviço e carro em excelente estado.'),
(5, 5, '2024-05-26', 4, 'Bom carro, mas o atendimento poderia ser melhor.');

-- Inserindo dados na tabela Reservas
INSERT INTO Reservas (usuario_id, veiculo_id, data_reserva, data_inicio, data_fim) VALUES
(1, 1, '2024-04-25', '2024-05-01', '2024-05-10'),
(2, 3, '2024-04-30', '2024-05-05', '2024-05-15'),
(3, 2, '2024-05-20', '2024-06-01', '2024-06-10'),
(4, 4, '2024-05-05', '2024-05-10', '2024-05-20'),
(5, 5, '2024-05-10', '2024-05-15', '2024-05-25');

-- Inserindo dados na tabela HistoricoPrecos
INSERT INTO HistoricoPrecos (veiculo_id, data_efetiva, tarifa_diaria, tarifa_semanal, tarifa_mensal) VALUES
(1, '2024-04-01', 50.00, 300.00, 1000.00),
(2, '2024-04-15', 60.00, 350.00, 1200.00),
(3, '2024-05-01', 55.00, 325.00, 1100.00),
(4, '2024-05-15', 70.00, 400.00, 1300.00),
(5, '2024-06-01', 65.00, 375.00, 1250.00);