# Python-flask-toolfetch-dan-ip-address-mikrotik
<html>
<body>
mendapatkan ip address dari mikrotik dan dikirim menggunakan tool fetch ke flask python:
<div>
<li>
1.membuat dhcp leases mikrotik yang dituliskan pada /ip dhcp-server lease-script dengan materi:
    <ul>
    a.foreach script mikrotik
    b.tool fetch mikrotik
    </ul>
2.membuat app.py dengan materi:
    <ul>
    a.flask
    b.request
    c.json
    d.render_template
    e.file append
    f.file read
    </ul>
3.membuat file ip_address.txt untuk menyimpan ip address yang diambil dari fetch mikrotik
4.membuat file index.html untuk menampilkan isi file ip_address.txt ke web browser
</li>
</body>
</html>