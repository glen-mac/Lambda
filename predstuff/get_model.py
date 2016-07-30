import pickle
import numpy as np


def load_model(path):
    """
    Loads pickle model for prediction stuff
    """
    return pickle.load(open(path, "rb"))


def predict(reg, features):
    """
    IN:
    reg: sklearn prediction model (pickle file)
    features: feature column vector

    features should be a numpy array or list with following format:
         'Gender', 'age_range',
         'Partner_status', 'Region',
         'Taxable_Income', 'Sw_amt',
         'Alow_ben_amt', 'ETP_txbl_amt',
         'Grs_int_amt', 'Aust_govt_pnsn_allw_amt',
         'Unfranked_Div_amt','Frk_Div_amt',
         'Dividends_franking_cr_amt', 'Net_rent_amt',
         'Gross_rent_amt', 'Other_rent_ded_amt',
         'Rent_int_ded_amt', 'Rent_cap_wks_amt',
         'Net_farm_management_amt','Net_PP_BI_amt',
         'Net_NPP_BI_amt','Total_PP_BI_amt',
         'Total_NPP_BI_amt','Total_PP_BE_amt',
         'Total_NPP_BE_amt','Net_CG_amt',
         'Tot_CY_CG_amt','Net_PT_PP_dsn',
         'Net_PT_NPP_dsn','Taxed_othr_pnsn_amt',
         'Untaxed_othr_pnsn_amt','Other_foreign_inc_amt',
         'Other_inc_amt','Tot_inc_amt', 'Occ_code'


    OUT: float of predicted tax deduction
    """
    reg_predict = reg.predict(features)
    return reg_predict[0]
