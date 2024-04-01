--------------------------------------------------------
--  颇老捞 积己凳 - 格夸老-3岿-21-2024   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table MEMBERTBL
--------------------------------------------------------

  CREATE TABLE "SHOP"."MEMBERTBL" 
   (	"MEMBERID" CHAR(8 BYTE), 
	"MEMBERNAME" NCHAR(5), 
	"MEMBERADDRESS" NVARCHAR2(20)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Trigger TRG_DELETEDMEMBERTBL
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "SHOP"."TRG_DELETEDMEMBERTBL" 
    after delete
    on membertbl
    for each row
begin
    insert into deletedmembertbl
    values (:old.memberid, :old.membername, :old.memberaddress, sysdate());
end;  

/
ALTER TRIGGER "SHOP"."TRG_DELETEDMEMBERTBL" ENABLE;
--------------------------------------------------------
--  Constraints for Table MEMBERTBL
--------------------------------------------------------

  ALTER TABLE "SHOP"."MEMBERTBL" MODIFY ("MEMBERNAME" NOT NULL ENABLE);
  ALTER TABLE "SHOP"."MEMBERTBL" MODIFY ("MEMBERID" NOT NULL ENABLE);
