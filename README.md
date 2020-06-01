# Python-flask-toolfetch-dan-ip-address-mikrotik
<html>
<body>
mendapatkan ip address dari mikrotik dan dikirim menggunakan tool fetch ke flask python:
<div>
<li>
1.membuat dhcp leases mikrotik yang dituliskan pada /ip dhcp-server lease-script dengan materi:
    <li>
    a.foreach script mikrotik
    b.tool fetch mikrotik
    </li>
2.membuat app.py dengan materi:
    <li>
    a.flask
    b.request
    c.json
    d.render_template
    e.file append
    f.file read
    </li>
3.membuat file ip_address.txt untuk menyimpan ip address yang diambil dari fetch mikrotik
4.membuat file index.html untuk menampilkan isi file ip_address.txt ke web browser
</li>
</body>
</html>