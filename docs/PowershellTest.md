## Powershell test


```
$udpClient = New-Object System.Net.Sockets.UdpClient
$message = [System.Text.Encoding]::ASCII.GetBytes("Your message here")
$udpClient.Send($message, $message.Length, "raspberrypi.local", 5005)
```
