CREATE DATABASE IF NOT EXISTS atividade3bd;
USE atividade3bd;


CREATE TABLE IF NOT EXISTS Clube (
  id_clube INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  cnpj VARCHAR(18) NOT NULL,
  cidade VARCHAR(45) NOT NULL,
  estado CHAR(2) NOT NULL,
  data_filiacao DATE NOT NULL,
  PRIMARY KEY (id_clube),
  UNIQUE KEY uq_clube_cnpj (cnpj)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS Jogador (
  id_jogador INT NOT NULL AUTO_INCREMENT,
  licenca INT NOT NULL,
  posicao VARCHAR(45) NOT NULL,
  altura INT NOT NULL,
  peso INT NOT NULL,
  primeiro_nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  telefones TEXT,
  PRIMARY KEY (id_jogador),
  UNIQUE KEY uq_jogador_licenca (licenca),
  UNIQUE KEY uq_jogador_cpf (cpf)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS Contrato (
  id_contrato VARCHAR(45) NOT NULL,
  id_jogador INT NOT NULL,
  id_clube INT NOT NULL,
  data_inicio DATE NOT NULL,
  data_fim DATE NOT NULL,
  salario DECIMAL(10,2) NOT NULL,
  multa DECIMAL(10,2),
  PRIMARY KEY (id_contrato),
  KEY idx_contrato_jogador (id_jogador),
  KEY idx_contrato_clube (id_clube),
  CONSTRAINT fk_contrato_jogador
    FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_contrato_clube
    FOREIGN KEY (id_clube) REFERENCES Clube(id_clube)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_datas
    CHECK (data_fim >= data_inicio)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


select *
from Clube;

