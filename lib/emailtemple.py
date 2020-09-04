templatefile = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <title></title>

  <style type="text/css">
  </style>    
</head>
<body style="margin:0; padding:0; background-color:#F2F2F2;">
  <center>
    <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
      <tr>
        <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
      </tr>
      <tr>
        <td align="center" valign="top">

          <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
            <tr>
              <td align="center" valign="top">
                <h3 style="Margin-top: 0;Margin-bottom: 0;">基本信息</h3>
              </td>
            </tr>
            <tr>
              <td align="left" valign="top">
                <li>主机名: {hostname}</li>
              </td>
            </tr>
            <tr>
              <td align="left" valign="top">
                <li>触发时间: {time}</li>
              </td>
            </tr>
            <tr>
              <td align="left" valign="top">
                <li>文件名称: {filename}</li>
              </td>
            </tr>
            <tr>
              <td align="left" valign="top">
                <li>文件动作: {maskname}</li>
              </td>
            </tr>
            <tr>
              <td align="left" valign="top">
                <li>文件路径: {filepath}</li>
              </td>
            </tr>

          </table>
            <p style="Margin-top: 0;Margin-bottom: 0;"><strong>&#25195;&#25551;&#20449;&#24687;&#35831;&#26597;&#30475;&#38468;&#20214; result.csv</strong></p>

        </td>
      </tr>
      <tr>
        <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
      </tr>
    </table>  
  </center>
</body>
</html>

"""