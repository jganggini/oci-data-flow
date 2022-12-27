import oci

# [Parameter:opt] OCI Data Flow
par_oci_opt_patch                  = '/opt/dataflow/python/lib/python3.6/site-packages/'
par_oci_obj_ociProfileName         = 'LOCAL'

# [Parameter:oci_adb] Autonomous Database
oci_adb_user_name_1                = "admin"
oci_adb_password_1                 = "]VGQH=wCg4iM"
oci_adb_service_name_1             = "adwdemo_high"
oci_adb_wallet_location_1          = (par_oci_opt_patch + 'src/.oci/adb/Wallet_adwdemo.zip' if par_oci_obj_ociProfileName=='DATAFLOW' else './src/.oci/adb/Wallet_adwdemo.zip')

# [Parameter:utl_log] Control
par_utl_log_bucket_name            = 'target-data'
par_utl_log_object_name            = ('log/log_dataflow_app.json' if par_oci_obj_ociProfileName=='DATAFLOW' else './log_dataflow_app.json')