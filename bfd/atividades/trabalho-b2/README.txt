Sistema de Biblioteca - Trabalho 2º Bimestre
Autor: Kauã de Andrade Rodrigues
Data Criação: 15/10/2025
Data Última Atualização: 29/10/2025
Atualização Feita por: Kauã de Andrade Rodrigues

Instruções de instalação:
1-Instale o python
2-Coloque a pasta "trabalho" em um diretório de sua preferência
3-Abra a pasta trabalho na sua IDE
4-Entre execute o venv
5-Entre no diretório biblioteca, lá se encontra o arquivo config.py
6-altere as configuração para o seu banco de dados
7-inicie uma conexão no mysql workbench
8-execute o arquivo main.py


Código SQL do banco de Dados:


CREATE SCHEMA IF NOT EXISTS `biblioteca` DEFAULT CHARACTER SET utf8 ;
USE `biblioteca` ;


CREATE TABLE IF NOT EXISTS `biblioteca`.`Livro` (
  `idLivro` INT NOT NULL,
  `titulo` VARCHAR(100) NOT NULL,
  `ISBN` INT NOT NULL,
  `ano` DATE NOT NULL,
  `nomeEditora` VARCHAR(50) NOT NULL,
  `nomeAutor` VARCHAR(50) NOT NULL,
  `status` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idLivro`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `biblioteca`.`Usuario` (
  `matricula` INT NOT NULL,
  `nome` VARCHAR(100) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`matricula`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `biblioteca`.`Emprestimo` (
  `idEmprestimo` INT NOT NULL,
  `dataRetirada` DATE NOT NULL,
  `dataDevolucaoPrevista` DATE NOT NULL,
  `dataDevolucaoReal` DATE NULL,
  `status` VARCHAR(20) NOT NULL,
  `idLivro` INT NOT NULL,
  `matriculaUsuario` INT NOT NULL,
  PRIMARY KEY (`idEmprestimo`, `idLivro`, `matriculaUsuario`),
  INDEX `fk_Emprestimo_Livro1_idx` (`idLivro` ASC) VISIBLE,
  INDEX `fk_Emprestimo_Usuario1_idx` (`matriculaUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_Emprestimo_Livro1`
    FOREIGN KEY (`idLivro`)
    REFERENCES `mydb`.`Livro` (`idLivro`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Emprestimo_Usuario1`
    FOREIGN KEY (`matriculaUsuario`)
    REFERENCES `biblioteca`.`Usuario` (`matricula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;