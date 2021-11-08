CREATE TABLE madhack_upc (
    upc_ean_plu varchar2(20),
    cost        decimal(10,2)
)

INSERT INTO madhacks_upc (upc_ean_plu, cost) VALUES ('37600138727',5.5);
INSERT INTO madhacks_upc (upc_ean_plu, cost) VALUES ('4103',1.5);
INSERT INTO madhacks_upc (upc_ean_plu, cost) VALUES ('4024',2.5);
COMMIT;

SELECT * FROM madhacks_upc;

Instalar cx_Oracle

python -m pip install cx_Oracle --upgrade --user

pip install urllib3

---------------------

BEGIN
  DBMS_CLOUD.create_credential (
    credential_name     => 'OBJ_STORE_CRED',
    username            => 'oracleidentitycloudservice/joel.ganggini@oracle.com',
    password            => 'p>]RN<cK2Jbr3Y:B3f2r'
  );
END;

BEGIN
  DBMS_CREDENTIAL.DROP_CREDENTIAL (
    'OBJ_STORE_CRED',
    FALSE
  );
END;

--https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/format-options.html#GUID-08C44CDA-7C81-481A-BA0A-F7346473B703

BEGIN  
 DBMS_CLOUD.COPY_COLLECTION(    
    collection_name => 'madhack_json_edamam',
    credential_name => 'OBJ_STORE_CRED',
    file_uri_list   =>
      'https://objectstorage.us-ashburn-1.oraclecloud.com/n/idlhjo6dp3bd/b/madhacks-target/o/edamam_food_database_api.json',
    format          =>
      JSON_OBJECT('unpackarrays' value 'true') );
END;
/

SELECT JSON_VALUE(obj.json_document,'$.food_foodId') FROM madhack_dataflow_edamam obj;


SELECT
    obj.json_document.upc_ean_plu as food_code,
    upc.cost as food_cost,
    obj.json_document.text as text_code,
    obj.json_document.food_foodId,
    obj.json_document.food_label,
    obj.json_document.food_nutrients_ENERC_KCAL,
    obj.json_document.food_nutrients_FAT,
    obj.json_document.food_nutrients_FASAT,
    obj.json_document.food_nutrients_FAMS,
    obj.json_document.food_nutrients_FAPU,
    obj.json_document.food_nutrients_CHOCDF,
    obj.json_document.food_nutrients_FIBTG,
    obj.json_document.food_nutrients_SUGAR,
    obj.json_document.food_nutrients_PROCNT,
    obj.json_document.food_nutrients_CHOLE,
    obj.json_document.food_nutrients_NA,
    obj.json_document.food_nutrients_CA,
    obj.json_document.food_nutrients_MG,
    obj.json_document.food_nutrients_K,
    obj.json_document.food_nutrients_FE,
    obj.json_document.food_nutrients_ZN,
    obj.json_document.food_nutrients_P,
    obj.json_document.food_nutrients_VITA_RAE,
    obj.json_document.food_nutrients_VITC,
    obj.json_document.food_nutrients_THIA,
    obj.json_document.food_nutrients_RIBF,
    obj.json_document.food_nutrients_NIA,
    obj.json_document.food_nutrients_VITB6A,
    obj.json_document.food_nutrients_FOLDFE,
    obj.json_document.food_nutrients_FOLFD,
    obj.json_document.food_nutrients_FOLAC,
    obj.json_document.food_nutrients_VITB12,
    obj.json_document.food_nutrients_VITD,
    obj.json_document.food_nutrients_TOCPHA,
    obj.json_document.food_nutrients_VITK1,
    obj.json_document.food_nutrients_WATER,
    obj.json_document.food_nutrients_VITC,
    obj.json_document.food_category,
    obj.json_document.food_categoryLabel,
    obj.json_document.food_foodContentsLabel,
    obj.json_document.food_image,
    obj.json_document.food_servingSizes_uri,
    obj.json_document.food_servingSizes_label,
    obj.json_document.food_servingSizes_quantity,
    obj.json_document.food_servingsPerContainer,
    obj.json_document.measures_uri,
    obj.json_document.measures_label,
    obj.json_document.measures_weight,
    obj.json_document.run_date,
    obj.json_document.run_id,
    obj.json_document.food_servingSizes_uri
FROM
    madhack_json_edamam obj
LEFT JOIN
    madhacks_upc upc
ON (upc.upc_ean_plu = obj.json_document.upc_ean_plu);