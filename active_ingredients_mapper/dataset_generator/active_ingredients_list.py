active_ingredients_list = [
    # Liver Diseases (Hepatitis B, Hepatitis C, Alcoholic Hepatitis, Chronic Hepatitis, Cirrhosis)
    ('Lamivudine', 'Tenofovir', 'Entecavir', 'Hepatitis B'),
    ('Lamivudine', 'Tenofovir', 'Entecavir', 'Hepatitis C'),
    ('Lamivudine', 'Tenofovir', 'Entecavir', 'Alcoholic Hepatitis'),
    ('Lamivudine', 'Tenofovir', 'Entecavir', 'Chronic Hepatitis'),
    ('Lamivudine', 'Tenofovir', 'Entecavir', 'Cirrhosis'),
    
    # Cardiovascular Diseases (Heart Disease, Stroke, Heart Attack, Atrial Fibrillation, Hyperlipidemia, Hypertension)
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Cardiovascular Disease'),
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Heart Disease'),
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Stroke'),
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Heart Attack'),
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Atrial Fibrillation'),
    ('Simvastatin', 'Atorvastatin', 'Rosuvastatin', 'Hyperlipidemia'),
    ('Aspirin', 'Clopidogrel', 'Beta-blockers', 'Heart Attack'),
    ('Aspirin', 'Clopidogrel', 'Beta-blockers', 'Stroke'),
    ('Aspirin', 'Clopidogrel', 'Beta-blockers', 'Cardiovascular Disease'),
    ('Enalapril', 'Atenolol', 'Losartan', 'Hypertension'),
    ('Enalapril', 'Atenolol', 'Losartan', 'Heart Failure'),
    ('Nitroglycerin', 'Isosorbide', '-', 'Angina'),
    ('Nitroglycerin', 'Isosorbide', '-', 'Heart Disease'),
    
    # Diabetes & Metabolic Disorders (Type 2 Diabetes, Type 1 Diabetes, Hypertension, Obesity, Hyperthyroidism, Hypothyroidism, Hyperlipidemia)
    ('Metformin', 'Sulfonylureas', '-', 'Diabetes'),
    ('Metformin', 'Sulfonylureas', '-', 'Type 2 Diabetes'),
    ('Metformin', 'Sulfonylureas', '-', 'Type 1 Diabetes'),
    ('Insulin', 'DPP-4 Inhibitors', '-', 'Diabetes'),
    ('Insulin', 'DPP-4 Inhibitors', '-', 'Type 2 Diabetes'),
    ('Levothyroxine', 'Liothyronine', 'Desiccated Thyroid', 'Hypothyroidism'),
    ('Levothyroxine', 'Liothyronine', 'Desiccated Thyroid', 'Goiter'),
    ('Enalapril', 'Atenolol', 'Losartan', 'Hypertension'),
    ('Orlistat', 'Phentermine', '-', 'Obesity'),
    
    # Headache & Migraines
    ('Ibuprofen', 'Paracetamol (Acetaminophen)', 'Aspirin', 'Headache'),
    ('Ibuprofen', 'Paracetamol (Acetaminophen)', 'Aspirin', 'Migraine'),
    ('Ibuprofen', 'Paracetamol (Acetaminophen)', 'Aspirin', 'Osteoarthritis'),
    ('Ibuprofen', 'Paracetamol (Acetaminophen)', 'Aspirin', 'Cervical Spondylosis'),
    ('Sumatriptan', 'Paracetamol', 'Ibuprofen', 'Migraine'),
    
    # Respiratory Diseases (Asthma, COPD, Pneumonia, Bronchitis, Chronic Bronchitis, Emphysema, Pulmonary Embolism)
    ('Salbutamol (Albuterol)', 'Ipratropium Bromide', 'Fluticasone', 'Asthma'),
    ('Salbutamol (Albuterol)', 'Ipratropium Bromide', 'Fluticasone', 'Chronic Obstructive Pulmonary Disease (COPD)'),
    ('Salbutamol (Albuterol)', 'Ipratropium Bromide', 'Fluticasone', 'Bronchitis'),
    ('Salbutamol (Albuterol)', 'Ipratropium Bromide', 'Fluticasone', 'Chronic Bronchitis'),
    ('Salbutamol (Albuterol)', 'Ipratropium Bromide', 'Fluticasone', 'Emphysema'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Pneumonia'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Bronchitis'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Respiratory Infections'),
    ('Hydrocortisone', 'Prednisone', 'Corticosteroids', 'Pulmonary Embolism'),
    
    # Gastrointestinal Disorders (Diarrhea, Gastroenteritis, Stomach Ulcer, Peptic Ulcer Disease, GERD, Irritable Bowel Syndrome, Crohn’s Disease)
    ('Loperamide (Imodium)', 'Diphenoxylate', 'Oral Rehydration Salts (ORS)', 'Diarrhea'),
    ('Loperamide (Imodium)', 'Diphenoxylate', 'Oral Rehydration Salts (ORS)', 'Gastroenteritis'),
    ('Omeprazole', 'Ranitidine', 'Esomeprazole', 'GERD'),
    ('Omeprazole', 'Ranitidine', 'Esomeprazole', 'Stomach Ulcer'),
    ('Omeprazole', 'Ranitidine', 'Esomeprazole', 'Peptic Ulcer Disease'),
    ('Sulfasalazine', 'Mesalamine', '-', 'Irritable Bowel Syndrome'),
    ('Sulfasalazine', 'Mesalamine', '-', 'Crohn’s Disease'),
    
    # Infectious Diseases (Tuberculosis, Dengue, Typhoid, Malaria, HIV/AIDS, Hepatitis B, Hepatitis C, Urinary Tract Infection, Pneumonia, Sepsis)
    ('Chloroquine', 'Artemisinin-based Combination Therapy (ACT)', 'Mefloquine', 'Malaria'),
    ('Ciprofloxacin', 'Nitrofurantoin', 'Amoxicillin', 'Typhoid'),
    ('Ciprofloxacin', 'Nitrofurantoin', 'Amoxicillin', 'Urinary Tract Infection'),
    ('Ciprofloxacin', 'Nitrofurantoin', 'Amoxicillin', 'Bacterial Infections'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Respiratory Infections'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Pneumonia'),
    ('Azithromycin', 'Levofloxacin', 'Doxycycline', 'Bronchitis'),
    ('Dexamethasone', 'Prednisone', 'Hydrocortisone', 'Dengue'),
    ('Lamivudine', 'Tenofovir', 'Efavirenz', 'HIV/AIDS'),
    ('Rifampicin', 'Isoniazid', 'Pyrazinamide', 'Tuberculosis'),
    
    # Skin Disorders (Acne, Psoriasis, Impetigo, Fungal Infections, Eczema, Dermatitis, Rosacea, Warts, Hives)
    ('Tretinoin', 'Benzoyl Peroxide', 'Salicylic Acid', 'Acne'),
    ('Tretinoin', 'Benzoyl Peroxide', 'Salicylic Acid', 'Psoriasis'),
    ('Tretinoin', 'Benzoyl Peroxide', 'Salicylic Acid', 'Wrinkles'),
    ('Clotrimazole', 'Ketoconazole', 'Miconazole', 'Fungal Infections'),
    ('Clotrimazole', 'Ketoconazole', 'Miconazole', 'Vaginal Yeast Infection'),
    ('Clotrimazole', 'Ketoconazole', 'Miconazole', 'Athlete’s Foot'),
    ('Mupirocin', 'Neomycin', '-', 'Impetigo'),
    ('Mupirocin', 'Neomycin', '-', 'Skin Infections'),
    ('Hydrocortisone', 'Betamethasone', 'Prednisone', 'Eczema'),
    ('Hydrocortisone', 'Betamethasone', 'Prednisone', 'Dermatitis'),
    ('Metronidazole', 'Clindamycin', '-', 'Rosacea'),
    ('Imiquimod', 'Cryotherapy', '-', 'Warts'),
    
    # Depression & Mental Health Disorders (Depression, Anxiety, Bipolar Disorder, PTSD, Schizophrenia, OCD)
    ('Bupropion', 'Fluoxetine', 'Sertraline', 'Depression'),
    ('Bupropion', 'Fluoxetine', 'Sertraline', 'Anxiety'),
    ('Bupropion', 'Fluoxetine', 'Sertraline', 'Bipolar Disorder'),
    ('Bupropion', 'Fluoxetine', 'Sertraline', 'PTSD'),
    ('Paracetamol (Acetaminophen)', 'Diphenhydramine', 'Ibuprofen', 'Common Cold'),
    ('Paracetamol (Acetaminophen)', 'Diphenhydramine', 'Ibuprofen', 'Headache'),
    ('Paracetamol (Acetaminophen)', 'Diphenhydramine', 'Ibuprofen', 'Body Aches'),
    ('Paracetamol (Acetaminophen)', 'Diphenhydramine', 'Ibuprofen', 'Fever'),
    ('Diazepam', 'Clonazepam', 'Alprazolam', 'Anxiety'),
    ('Lithium', 'Valproate', 'Lamotrigine', 'Bipolar Disorder'),
    ('Olanzapine', 'Risperidone', 'Clozapine', 'Schizophrenia'),
    ('Fluoxetine', 'Sertraline', 'Trazodone', 'OCD'),
    
    # Common Cold (Upper Respiratory Tract Infection)
    ('Paracetamol (Acetaminophen)', 'Diphenhydramine', 'Ibuprofen', 'Common Cold'),
    
    # COVID
    ('Hydroxychloroquine', 'Remdesivir', 'Dexamethasone', 'COVID'),
    
    # Cancer (Breast Cancer, Lung Cancer, Leukemia, Prostate Cancer, Colorectal Cancer, Ovarian Cancer, Skin Cancer, Lymphoma)
    ('Methotrexate', 'Cyclophosphamide', 'Cancer', 'Rheumatoid Arthritis'),
    ('Tamoxifen', 'Anastrozole', 'Trastuzumab', 'Breast Cancer'),
    ('Carboplatin', 'Paclitaxel', 'Cisplatin', 'Lung Cancer'),
    ('Imatinib', 'Dasatinib', '-', 'Leukemia'),
    ('Bicalutamide', 'Docetaxel', '-', 'Prostate Cancer'),
    ('FOLFOX', 'Bevacizumab', '-', 'Colorectal Cancer'),
    ('Paclitaxel', 'Cisplatin', '-', 'Ovarian Cancer'),
    ('Doxorubicin', 'Vincristine', '-', 'Skin Cancer'),
    ('Rituximab', 'Chlorambucil', '-', 'Lymphoma'),
    
    # Additional related categories
    ('Vitamin B12', 'Iron Supplements', 'Folic Acid', 'Anemia'),
    ('Vitamin B12', 'Iron Supplements', 'Folic Acid', 'Fatigue'),
    ('Vitamin B12', 'Iron Supplements', 'Folic Acid', 'Nerve Disorders'),
    ('Zinc Supplements', 'Vitamin C', 'Echinacea', 'Immune System Support'),
    ('Zinc Supplements', 'Vitamin C', 'Echinacea', 'Common Cold'),
    ('Zinc Supplements', 'Vitamin C', 'Echinacea', 'Skin Health'),
    ('Erythropoietin', 'G-CSF', '-', 'Neutropenia'),
    ('Erythropoietin', 'G-CSF', '-', 'Anemia'),
    ('Probenecid', 'Allopurinol', '-', 'Gout'),
    ('Probenecid', 'Allopurinol', '-', 'Hyperuricemia'),
    ('Furosemide', 'Spironolactone', '-', 'Heart Failure'),
    ('Furosemide', 'Spironolactone', '-', 'Chronic Kidney Disease')
]
