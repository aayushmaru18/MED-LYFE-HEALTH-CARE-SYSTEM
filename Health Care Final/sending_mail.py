import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "medlyfe24.7@gmail.com"
password = "marutayadesejpal"
#receiver_email = "aayushmaru18@gmail.com"

def send_email(receiver_email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to MED LYFE 24/7"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hey,
    We are from MED LYFE 24/7.
    """
    html = """


    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

    <head>
        <meta charset="UTF-8">
        <meta content="width=device-width, initial-scale=1" name="viewport">
        <meta name="x-apple-disable-message-reformatting">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta content="telephone=no" name="format-detection">
        <title></title>
        <!--[if (mso 16)]>
        <style type="text/css">
        a {text-decoration: none;}
        </style>
        <![endif]-->
        <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
        <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
        <o:AllowPNG></o:AllowPNG>
        <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    </head>

    <body>
        <div class="es-wrapper-color">
            <!--[if gte mso 9]>
                <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
                    <v:fill type="tile" src="https://tlr.stripocdn.email/content/guids/CABINET_26a0436290e8d4bfb62f4a7669434c8d/images/17491585651509606.png" color="#eef4f4"></v:fill>
                </v:background>
            <![endif]-->
            <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="background-position: left top;" background="https://tlr.stripocdn.email/content/guids/CABINET_26a0436290e8d4bfb62f4a7669434c8d/images/17491585651509606.png">
                <tbody>
                    <tr>
                        <td class="esd-email-paddings" valign="top">
                            <table cellpadding="0" cellspacing="0" class="es-content esd-header-popover" align="center">
                                <tbody>
                                    <tr>
                                        <td class="esd-stripe" align="center">
                                            <table bgcolor="rgba(0, 0, 0, 0)" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p10t es-p10b es-p20r es-p20l" align="left">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td class="esd-block-text es-infoblock es-m-txt-c" align="left">
                                                                                            <p><strong>Health Care for the future</strong></p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                                <tbody>
                                    <tr>
                                        <td class="esd-stripe" align="center" bgcolor="transparent" style="background-color: transparent;">
                                            <table bgcolor="#ffffff" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure" align="left" esd-custom-block-id="112652">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-image" style="font-size: 0px;"><a target="_blank"><img class="adapt-img" src="https://turnaround.org/sites/default/files/Screen%20Shot%202019-01-16%20at%202.18.26%20PM.png" alt style="display: block;" width="600"></a></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="esd-structure es-p10t es-p20b es-p20r es-p20l" align="left" style="background-color: #ffffff;" bgcolor="#ffffff" esd-custom-block-id="112657">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="560" class="esd-container-frame" align="left">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-text es-m-txt-c">
                                                                                            <h2 style="font-size: 28px; color: #00b7c1;">MED LYFE 24/7</h2>
                                                                                        </td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-text es-p10t es-p15b">
                                                                                            <p style="color: #3dc3d0; line-height: 100%;">Hey,<br>Thank -You for registering on MED LYFE 24/7!<br>We are here to predict your disease from the symptoms using our Machine Learning Web Application. We have suggested some remedies for the same.<br><br><br><br></p>
                                                                                        </td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-button es-p10">
                                                                                            <!--[if mso]><a href="https://viewstripo.email/" target="_blank">
        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" stripoVmlButton href="https://viewstripo.email/" 
                    style="height:43px;v-text-anchor:middle;width:103px;" arcsize="7%" stroke="f"  fillcolor="#00b7c1">
            <w:anchorlock></w:anchorlock>
            <center style='color:#ffffff;font-family:arial, "helvetica neue", helvetica, sans-serif;font-size:15px;font-weight:bold;'>VISIT US</center>
        </v:roundrect></a>
    <![endif]-->
                                                                                            <!--[if !mso]><!-- --><span class="msohide es-button-border"><a href="https://viewstripo.email/" class="es-button" target="_blank">VISIT US</a></span>
                                                                                            <!--<![endif]-->
                                                                                        </td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="esd-structure" align="left" style="background-position: center top; background-color: #eef4f4;" bgcolor="#eef4f4">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="600" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-image" style="font-size:0"><a target="_blank"><img class="adapt-img" src="https://tlr.stripocdn.email/content/guids/CABINET_26a0436290e8d4bfb62f4a7669434c8d/images/74001567514648241.png" alt style="display: block;" width="600"></a></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>

    </html>

    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )