/*

****   No programa Python, tem que importar o MySQLdb , e tem que ter esta pasta no projeto(Pasta do Projeto\Lib\MySQLdb)
import MySQLdb


drop table alunos 
drop table cursos 
drop table notas
drop  table alunos_curso 
                             
create table alunos ( id_aluno int not null auto_increment, primary key(id_aluno));
create table cursos ( id_curso int not null auto_increment, primary key(id_curso));
create table notas ( id_nota int not null auto_increment, primary key(id_nota));
create  table alunos_curso ( id_aluno_curso  int not null auto_increment primary key,
                             id_aluno int not null , id_curso int not null ) 

*/

/*
To change column a from INTEGER to TINYINT NOT NULL (leaving the name the same), 
      and to change column b from CHAR(10) to CHAR(20) as well as renaming it from b to c: 
ex.:
ALTER TABLE t2 MODIFY a TINYINT NOT NULL, CHANGE b c CHAR(20);

*/
create table alunos ( id_aluno int not null auto_increment, primary key(id_aluno));
alter table alunos add column  ( nome varchar(100) not null , data_nascimento date not null , 
                                                      endereco varchar(255)  not null, cidade varchar(100) not null,
                                                      estado varchar(2) not null, CPF varchar(11) not null );
                                                      
create table cursos ( id_curso int not null auto_increment, primary key(id_curso));
alter table cursos add column  ( nome varchar(100) not null );
                                                      
                                                      
create   table notas ( id_nota int not null auto_increment, primary key(id_nota));
alter table notas add column  ( descricao_atividade varchar(100) not null, valor_nota decimal not null);
alter table notas MODIFY valor_nota decimal(5,2) not null;


/*
-- Criando na tab alunos_curso chaves e primárias 
alter table alunos_curso add index fk_id_aluno_idx(id_aluno asc) visible
alter table alunos_curso add index fk_id_curso_idx(id_curso asc) visible

-- Criando na tab alunos_curso 1ºchave estrangeira
alter table alunos_curso 
         add constraint fk_id_aluno
          foreign key (id_aluno) references alunos(id_aluno) 
         on delete no action 
         on update no action 
         
-- Criando na tab alunos_curso   2ºchave estrangeira          
alter table alunos_curso 
         add constraint fk_id_curso 
          foreign key (id_curso) references cursos(id_curso) 
         on delete no action 
         on update no action       
         
-- Criando chaves e indices e chave sna tab notas
alter table notas add column id_aluno_curso int not null  after id_nota
alter table notas add  index fk_id_aluno_curso_idx(id_aluno_curso asc) visible
   
alter table notas 
                         add  constraint fk_id_aluno_curso
                           foreign key (id_aluno_curso) references alunos_curso(id_aluno_curso)
                          on delete no action 
					  	on update no action                       

*/

/*  Alimentando as tabelas
insert into alunos values ( default, 'Pedro Martins','1987/07/17', 'Av.Antonio Carlos 6673','Belo Horizonte','MG', '07347812111')
insert into alunos values ( default, 'Ataíde Antonio','1965/09/05', 'Av.Praia da Luz 06 ','Sao Paulo','SP'  , '04534812111')
insert into alunos values ( default, 'Jose Andrade','2001/07/21', 'Av.José Paulo 1232','Itaju','SP', '34244548932')
insert into alunos values ( default, 'Monica Garibaldi', '2006/03/12' , ' Rua XV de Maioo 132','Itaju','SP', '56244548790')
insert into alunos values ( default, 'Rose Andraus ','2011/05/24', 'Av.Andre Saulo 4432','Itapolis','RJ', '26544548987')

select * from alunos

-- Atenção ao inserir chaves estrangeiras que não existem:
insert  into cursos values ( default, 'Codeigniter') , 	( default, 'Python') , 	( default, 'MySql') 
select * from cursos

 insert into alunos_curso values
        (default, 1,1),  (default, 1,2),   (default, 2,1),  (default, 2,3), 
        (default, 3,1), (default, 3,2 ), (default, 4,1),  (default, 5,1)
  select * from alunos_curso        

 insert into notas  values
          (default, 1,'Prova 1', 28.0),             (default, 3,'Prova 1', 25.0),            (default, 5,'Prova 1', 28.0),  
           (default, 2,'Exercicio 1', 10.0),       (default, 6,'Exercicio 2', 12.0),      (default, 1,'Prova 2', 22.0),  
           (default, 2,'Prova 2', 20.0)
           
   select * from notas

*/


