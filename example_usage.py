from client import AlgorithmicUsedCarValuationFinancingMarketplaceClient

def main():
    client = AlgorithmicUsedCarValuationFinancingMarketplaceClient()
    res = client.evaluate_and_finance_vehicle('3N1AB7AP4HY291048', 35000, 2023)
    print('VIN: ' + res['vin'] + ' | Valuation: $' + str(res['instant_buyout_offer_usd']) + ' (Inspection: ' + str(res['inspection_score_240_point']) + '/240)')
    fin = res['financing_preapproval']
    print('Financing: $' + str(fin['monthly_payment_usd']) + '/mo @ ' + str(fin['apr_pct']) + '% APR (' + str(fin['loan_term_months']) + ' mos)')
    print('Warranty: ' + str(res['certified_warranty_months']) + ' months certified coverage')

if __name__ == '__main__':
    main()
