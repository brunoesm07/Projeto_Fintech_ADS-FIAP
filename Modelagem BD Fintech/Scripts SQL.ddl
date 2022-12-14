-- Gerado por Oracle SQL Developer Data Modeler 22.2.0.165.1149
--   em:        2022-11-09 18:43:28 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE conta (
    id_conta           NUMBER NOT NULL,
    balanco            FLOAT NOT NULL,
    saldo_receita      FLOAT NOT NULL,
    saldo_despesa      FLOAT NOT NULL,
    usuario_id_usuario NUMBER NOT NULL
);

ALTER TABLE conta ADD CONSTRAINT conta_pk PRIMARY KEY ( id_conta,
                                                        usuario_id_usuario );

CREATE TABLE despesa (
    id_despesa                  NUMBER NOT NULL,
    lancamento_descricao        VARCHAR2(60) NOT NULL,
    lanc_con_id_conta           NUMBER NOT NULL,
    lanc_con_usuario_id_usuario NUMBER NOT NULL
);

CREATE UNIQUE INDEX despesa__idx ON
    despesa (
        lancamento_descricao
    ASC,
        lanc_con_id_conta
    ASC,
        lanc_con_usuario_id_usuario
    ASC );

CREATE TABLE lancamento (
    descricao                VARCHAR2(60) NOT NULL,
    dia                      DATE NOT NULL,
    categoria                VARCHAR2(30),
    valor                    FLOAT NOT NULL,
    anexo                    BLOB,
    conta_id_conta           NUMBER NOT NULL,
    conta_usuario_id_usuario NUMBER NOT NULL
);

ALTER TABLE lancamento
    ADD CONSTRAINT lancamento_pk PRIMARY KEY ( descricao,
                                               conta_id_conta,
                                               conta_usuario_id_usuario );

CREATE TABLE receita (
    id_receita                  NUMBER NOT NULL,
    lancamento_descricao        VARCHAR2(60) NOT NULL,
    lanc_con_id_conta           NUMBER NOT NULL,
    lanc_con_usuario_id_usuario NUMBER NOT NULL
);

CREATE UNIQUE INDEX receita__idx ON
    receita (
        lancamento_descricao
    ASC,
        lanc_con_id_conta
    ASC,
        lanc_con_usuario_id_usuario
    ASC );

CREATE TABLE usuario (
    id_usuario NUMBER NOT NULL,
    nome       VARCHAR2(60) NOT NULL,
    email      VARCHAR2(60) NOT NULL,
    senha      VARCHAR2(16) NOT NULL
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( id_usuario );

ALTER TABLE conta
    ADD CONSTRAINT conta_usuario_fk FOREIGN KEY ( usuario_id_usuario )
        REFERENCES usuario ( id_usuario );

ALTER TABLE despesa
    ADD CONSTRAINT despesa_lancamento_fk FOREIGN KEY ( lancamento_descricao,
                                                       lanc_con_id_conta,
                                                       lanc_con_usuario_id_usuario )
        REFERENCES lancamento ( descricao,
                                conta_id_conta,
                                conta_usuario_id_usuario );

ALTER TABLE lancamento
    ADD CONSTRAINT lancamento_conta_fk FOREIGN KEY ( conta_id_conta,
                                                     conta_usuario_id_usuario )
        REFERENCES conta ( id_conta,
                           usuario_id_usuario );

ALTER TABLE receita
    ADD CONSTRAINT receita_lancamento_fk FOREIGN KEY ( lancamento_descricao,
                                                       lanc_con_id_conta,
                                                       lanc_con_usuario_id_usuario )
        REFERENCES lancamento ( descricao,
                                conta_id_conta,
                                conta_usuario_id_usuario );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             5
-- CREATE INDEX                             2
-- ALTER TABLE                              7
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
