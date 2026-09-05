#!/usr/bin/env python
                <div class="header">
                    <h1>🔬 Cell & Gene Therapy Monitor</h1>
                    <p>Setup Verification Email</p>
                </div>
                
                <div class="section">
                    <h2>✅ System Status: <span class="success">ACTIVE</span></h2>
                    <p>Your Cell & Gene Therapy Monitor is configured and working!</p>
                </div>
                
                <div class="section">
                    <h3>📊 What You're Monitoring</h3>
                    <ul>
                        <li>🚀 CAR-T Cell Therapy - All cancer indications</li>
                        <li>🧬 DNA-LNP Gene Therapy - All diseases</li>
                        <li>🧬 In Vivo DNA Delivery</li>
                        <li>📚 High-Impact Publications (IF≥10)</li>
                        <li>💼 M&A & Funding Announcements</li>
                    </ul>
                </div>
                
                <div class="section">
                    <h3>⏰ Schedule</h3>
                    <p><strong>Daily at 6:00 AM UTC</strong> - Data collection & alert check</p>
                    <p><strong>Weekly Monday at 8:00 AM UTC</strong> - Comprehensive digest</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "✅ Cell & Gene Therapy Monitor - Setup Verified"
        message["From"] = sender_email
        message["To"] = recipient_email
        
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)
        
        print(f"\n📧 Sending test email...")
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [recipient_email], message.as_string())
        
        print("✅ Email sent successfully!")
        print(f"\n📨 Check {recipient_email} inbox for the email")
        print("   (May take 1-2 minutes to arrive)")
        print("\n" + "=" * 80)
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return False


if __name__ == "__main__":
    success = send_test_email()
    sys.exit(0 if success else 1)