from analyzer import fetch_article_text, generate_report

if __name__ == "__main__":
    url = "https://www.moengage.com/casestudy/oyo-push-amplification-case-study/"  # Replace with the target article URL

    try:
        print("🔍 Fetching content...")
        text = fetch_article_text(url)
        print("✅ Generating report...")
        generate_report(url, text)
        print("📄 Report saved at: report_output/result.md")
    except Exception as e:
        print("❌ Error:", str(e))
