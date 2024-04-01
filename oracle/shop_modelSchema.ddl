-- 생성자 Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   위치:        2024-03-21 11:22:13 KST
--   사이트:      Oracle Database 11g
--   유형:      Oracle Database 11g



CREATE USER shop IDENTIFIED BY ACCOUNT UNLOCK ;

CREATE USER system IDENTIFIED BY ACCOUNT UNLOCK ;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE shop.membertbl (
    memberid      CHAR(8 BYTE) NOT NULL,
    membername    NCHAR(5) NOT NULL,
    memberaddress NVARCHAR2(20)
)
PCTFREE 10 PCTUSED 40 TABLESPACE users LOGGING
    STORAGE ( INITIAL 65536 NEXT 1048576 PCTINCREASE 0 MINEXTENTS 1 MAXEXTENTS 2147483645 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT
    );

CREATE TABLE shop.producttbl (
    productname NCHAR(4) NOT NULL,
    column1     NUMBER(7) NOT NULL,
    makedate    DATE,
    column2     NCHAR(5),
    amount      NUMBER(3)
)
PCTFREE 10 PCTUSED 40 TABLESPACE users LOGGING
    STORAGE ( INITIAL 65536 NEXT 1048576 PCTINCREASE 0 MINEXTENTS 1 MAXEXTENTS 2147483645 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT
    );

CREATE OR REPLACE PROCEDURE SHOP.MYPROC
as
    var1 int;
    var2 int;
begin
    select count(*) into var1 from membertbl;
    select count(*) into var2 from producttbl;
    dbms_output.put_line(var1+var2);
end;
/

CREATE TABLE shop.deletedmembertbl (
    memberid      CHAR(8 BYTE),
    membername    NCHAR(5),
    memberaddress NVARCHAR2(20),
    deleteddate   DATE
)
PCTFREE 10 PCTUSED 40 TABLESPACE users LOGGING
    STORAGE ( INITIAL 65536 NEXT 1048576 PCTINCREASE 0 MINEXTENTS 1 MAXEXTENTS 2147483645 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT
    );

CREATE TABLE shop.indextbl (
    first_name VARCHAR2(20 BYTE),
    last_name  VARCHAR2(25 BYTE) NOT NULL,
    hire_date  DATE NOT NULL
)
PCTFREE 10 PCTUSED 40 TABLESPACE users LOGGING
    STORAGE ( INITIAL 65536 NEXT 1048576 PCTINCREASE 0 MINEXTENTS 1 MAXEXTENTS 2147483645 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT
    );

CREATE INDEX system.idx_indextbl_firstname ON
    shop.indextbl (
        first_name
    ASC )
        TABLESPACE system PCTFREE 10
            STORAGE ( INITIAL 65536 NEXT 1048576 PCTINCREASE 0 MINEXTENTS 1 MAXEXTENTS 2147483645 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL
            DEFAULT )
        LOGGING;

CREATE OR REPLACE VIEW SHOP.MEMBERTBL_VIEW ( MEMBERNAME, MEMBERADDRESS ) AS
select membername, memberaddress from shop.membertbl 
;

CREATE OR REPLACE TRIGGER SHOP.TRG_DELETEDMEMBERTBL 
    AFTER DELETE ON SHOP.MEMBERTBL 
    FOR EACH ROW 
begin
    insert into deletedmembertbl
    values (:old.memberid, :old.membername, :old.memberaddress, sysdate());
end; 
/



-- Oracle SQL Developer Data Modeler 요약 보고서: 
-- 
-- CREATE TABLE                             4
-- CREATE INDEX                             1
-- ALTER TABLE                              0
-- CREATE VIEW                              1
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         1
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
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
-- CREATE USER                              2
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
