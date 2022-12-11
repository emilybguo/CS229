import pandas as pd
import random


def add_indicators(df, column):
    new_df = pd.DataFrame(index=range(len(df)))
    unique = df[column].unique()
    num_unique = len(unique)
    if num_unique == 1:
        return new_df
    for i in range(num_unique - 1):
        new_df[column + ':' + str(unique[i])] = 0

        for j in range(len(df)):
            if df.iloc[j][column] == unique[i]:
                new_df.at[j, column + ':' + str(unique[i])] = 1
    return new_df


def main():
    df = pd.read_csv(r'C:\Users\okayy\OneDrive\Desktop\School\Year 4\Q1\CS 229\Final Project\5216fb328d1d6394d342023c1e4c11bb (1).csv', low_memory=False)
    print("line: 22 ", len(df))
    df = df[(df['action_taken'] == 6) | (df['action_taken'] == 2) | (df['action_taken'] == 3)]
    df = df[df['reverse_mortgage'] == 2]
    df = df[(df['loan_type'] == 1) | (df['loan_type'] == 2)]
    df = df[df['loan_purpose'] == 1]


    df = df[df['derived_race'] != 'Race Not Available']
    df = df[df['derived_race'] != 'Free Form Text Only']
    df = df[df['derived_sex'] != 'Sex Not Available']
    df = df[df['derived_ethnicity'] != 'Ethnicity Not Available']
    df = df[df['derived_ethnicity'] != 'Free Form Text Only']
    df = df[(df['applicant_age'] != '8888')]
    df = df[df['debt_to_income_ratio'] != 'Exempt']
    df = df[df['initially_payable_to_institution'] != 'Exempt']
    df = df[df['submission_of_application'] != 'Exempt']
    df = df[df['applicant_credit_score_type'] != 'Exempt']
    df = df[df['property_value'] != 'Exempt']
    df = df[df['manufactured_home_land_property_interest'] != 'Exempt']
    df = df[df['manufactured_home_secured_property_type'] != 'Exempt']
    df = df[df['other_nonamortizing_features'] != 'Exempt']
    df = df[df['balloon_payment'] != 'Exempt']
    df = df[df['interest_only_payment'] != 'Exempt']
    df = df[df['negative_amortization'] != 'Exempt']
    df = df[df['business_or_commercial_purpose'] != 'Exempt']
    df = df[df['open-end_line_of_credit'] != 'Exempt']
    df = df.fillna(0)
    print("line: 47 ", len(df))
    print("line: 48 ", df.shape[0])

    df = df[["conforming_loan_limit", "derived_dwelling_category",
                  "derived_ethnicity", "derived_race", "derived_sex","lien_status",
                  "business_or_commercial_purpose", "loan_amount",
                  "loan_to_value_ratio", "interest_rate",
                  "rate_spread", "hoepa_status", "total_loan_costs",
                  "origination_charges", "discount_points", "lender_credits",
                  "loan_term", "negative_amortization", "interest_only_payment",
                  "balloon_payment", "other_nonamortizing_features",
                  "property_value", "construction_method", "occupancy_type",
                  "manufactured_home_secured_property_type",
                  "manufactured_home_land_property_interest",
                  "income", "debt_to_income_ratio", "applicant_age",
                  "applicant_ethnicity_observed", "applicant_race_observed",
                  "applicant_sex_observed", "initially_payable_to_institution",
                  "tract_minority_population_percent",
                  "tract_population", "co-applicant_ethnicity-1",
                  "ffiec_msa_md_median_family_income", "tract_to_msa_income_percentage",
                  "tract_median_age_of_housing_units", "applicant_credit_score_type",
                  "submission_of_application", "preapproval", "action_taken", "open-end_line_of_credit", "loan_type",
                  "prepayment_penalty_term", "intro_rate_period"]]

    category = ["conforming_loan_limit", "derived_dwelling_category",
                "derived_ethnicity", "derived_race", "derived_sex", "lien_status",
                "business_or_commercial_purpose", "hoepa_status", "negative_amortization", "interest_only_payment",
                "balloon_payment", "other_nonamortizing_features", "construction_method", "occupancy_type",
                "manufactured_home_secured_property_type", "manufactured_home_land_property_interest",
                "applicant_ethnicity_observed", "applicant_race_observed","applicant_sex_observed",
                "initially_payable_to_institution", "applicant_credit_score_type", "submission_of_application",
                "open-end_line_of_credit", "preapproval", "loan_type"]

    num_categorical = len(category)

    print("line: 82 ", len(df))
    for i in range(num_categorical):
        new_df = add_indicators(df, category[i])
        for value in new_df.columns.values.tolist():
            df[value] = new_df[value].values
        df = df.drop(columns=[category[i]])

    df.to_csv("hotcoded.csv")

    print("line: 89 ", len(df))

    df.loc[df['co-applicant_ethnicity-1'] != 5, 'co-applicant_ethnicity-1'] = 1
    df.loc[df['co-applicant_ethnicity-1'] == 5, 'co-applicant_ethnicity-1'] = 0
    df.rename(columns={'co-applicant_ethnicity-1': 'co-applicant'}, inplace=True)

    applicant_age = {
        "<25": 20,
        "25-34": 30,
        "35-44": 40,
        "45-54": 50,
        "55-64": 60,
        "65-74": 70,
        ">74": 80
    }

    debt_to_income_ratio = {
        0: 0,
        "0": 0,
        "<20%": 15,
        "20%-<30%": 25,
        "30%-<36%": 33,
        "36": 36,
        "37": 37,
        "38": 38,
        "39": 39,
        "40": 40,
        "41": 41,
        "42": 42,
        "43": 43,
        "44": 44,
        "45": 45,
        "46": 46,
        "47": 47,
        "48": 48,
        "49": 49,
        "50%-60%": 55,
        ">60%": 70
    }

    df["applicant_age"] = df["applicant_age"].apply(lambda x:applicant_age[x])
    df["debt_to_income_ratio"] = df["debt_to_income_ratio"].apply(lambda x: debt_to_income_ratio[x])
    print("line 137", len(df))
    df.to_csv("testingggggg.csv")

    print("line: 142 ", len(df))
    print(df.shape[0])



if __name__ == '__main__':
    main()