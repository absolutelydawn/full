-- 생성자 Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   위치:        2024-03-21 10:51:06 KST
--   사이트:      Oracle Database 11g
--   유형:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE buytbl (
    idnum          NUMBER(8) NOT NULL,
    userid         CHAR(8) NOT NULL,
    prodname       NCHAR(8) NOT NULL,
    groupname      NCHAR(4),
    price          NUMBER(8) NOT NULL,
    amount         NUMBER(3) NOT NULL,
    usertbl_userid CHAR(8) NOT NULL
);

ALTER TABLE buytbl ADD CONSTRAINT buytbl_pk PRIMARY KEY ( idnum );

CREATE TABLE usertbl (
    userid    CHAR(8) NOT NULL,
    username  NVARCHAR2(10) NOT NULL,
    birthyear NUMBER(4) NOT NULL,
    addr      NCHAR(2) NOT NULL,
    mobile1   CHAR(3),
    mobile2   CHAR(8),
    height    NUMBER(3),
    mdate     DATE
);

ALTER TABLE usertbl ADD CONSTRAINT usertbl_pk PRIMARY KEY ( userid );

ALTER TABLE buytbl
    ADD CONSTRAINT buytbl_usertbl_fk FOREIGN KEY ( usertbl_userid )
        REFERENCES usertbl ( userid );



-- Oracle SQL Developer Data Modeler 요약 보고서: 
-- 
-- CREATE TABLE                             2
-- CREATE INDEX                             0
-- ALTER TABLE                              3
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
