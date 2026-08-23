class AlgorithmicUsedCarValuationFinancingMarketplaceClient:
    def evaluate_and_finance_vehicle(self, vin='3N1AB7AP4HY291048', mileage_km=42000, model_year=2022):
        base_val = 18500.0
        depreciation = (mileage_km / 10000.0) * 450.0
        valuation = max(base_val - depreciation, 8000.0)
        return {
            'vin': vin,
            'model_year': model_year,
            'mileage_km': mileage_km,
            'instant_buyout_offer_usd': valuation,
            'inspection_score_240_point': 96.5,
            'financing_preapproval': {
                'monthly_payment_usd': 295.0,
                'loan_term_months': 48,
                'apr_pct': 6.8,
                'instant_approval': True
            },
            'certified_warranty_months': 12
        }
