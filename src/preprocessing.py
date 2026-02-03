import pandas as pd
import re

RAW_PATH="data/raw/wwr_jobs.csv"
CLEANED_PATH="data/preprocessed/wwr_jobs_cleaned.csv"

def clean_text(text):
    if pd.isna(text):
        return ""
    text= text.lower()
    text=re.sub(r'[^\w\s/+.-]', "", text)
    return text

def categorize_job(title, description=""):
    text = (title + " " + description).lower()
    
    if any(k in text for k in ["backend","server","api","python","java","node.js","php","c++","rails","django","flask","golang"]):
        return "Back-End"
    elif any(k in text for k in ["frontend","ui","ux","javascript","react","vue","angular","html","css"]):
        return "Front-End"
    elif any(k in text for k in ["fullstack","full-stack","full stack"]):
        return "Full-Stack"
    elif any(k in text for k in ["devops","cloud","infrastructure","sre","aws","azure","gcp","ci/cd","docker","kubernetes","terraform","sysadmin"]):
        return "DevOps / Sysadmin"
    elif any(k in text for k in ["support","customer service","helpdesk","client success","csr"]):
        return "Customer Support"
    elif any(k in text for k in ["sales","marketing","account executive","business development","growth","social media","crm","ppc"]):
        return "Sales / Marketing"
    elif any(k in text for k in ["designer","ui/ux","graphic","visual","product designer","illustrator","motion graphics","art director","3d","cad"]):
        return "Design"
    elif any(k in text for k in ["manager","finance","accountant","analyst","director","vp","cfo","strategy","project manager"]):
        return "Management / Finance"
    elif any(k in text for k in ["product","qa","quality assurance","tester","scrum"]):
        return "Product"
    else:
        return "Other"



def preprocess():
    df = pd.read_csv(RAW_PATH)

    df["job_title"] = df["job_title"].apply(clean_text)
    df["company"] = df["company"].apply(clean_text)
    df["location"] = df["location"].fillna("remote").apply(clean_text)

    df["job_category"] = df["job_title"].apply(categorize_job)

    df.to_csv(CLEANED_PATH, index=False)
    print(f"Preprocessed data saved to {CLEANED_PATH}")

if __name__ == "__main__":
    preprocess()

