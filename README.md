# snakeInventory
Link Adaptable: https://serpentshaven.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py,
   views.py, models.py, dan berkas html.
    HTTP request -->  urls.py
                        |
                        v
models.py   <-- -->  views.py --> HTTP response
                        ʌ
                        |
                   templates.py
    
    Setelah client melakukan HTTP request kepada URL, akan dicari pattern yang sesuai pada urls.py lalu akan dipanggil fungsi atau class pada
    views.py yang sesuai. Jika ada data yang dibutuhkan, proses akan dilanjut ke models.py yang menyediakan data tersebut. Setelah itu akan
    dikembalikan kepada views.py yang akan memberikan HTTP response yang mengandung berkas HTML kembali kepada client.


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual
   environment?
   Virtual environment digunakan untuk meng-install package dan library yang dibutuhkan untuk suatu projek tanpa memengaruhi projek lain. Misal,
   jika pada projek 1, dibutuhkan package A versi 1, namun pada projek 2 dibutuhkan package A versi 2, dengan menggunakan virtual environment, hal
   tersebut bisa dilakukan sehingga tidak terjadi conflict. Jika virtual environment tidak digunakan saat membuat suatu projek, semua package dan
   library akan digunakan secara global. Walau tidak menggunakan virtual environment bisa dilakukan, hal tersebut tidak dianjurkan agar bisa
   menghindari conflict yang mungkin terjadi.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC. MVT, dan MVVM merupakan pola arsitektur yang digunakan pada pengembangan perangkat lunak yang mengimplementasikan separation of concern,
    yaitu konsep dimana komponen yang berkaitan akan dijadikan suatu kesatuan dan dipisah dari kelompok komponen lainnya.
    
    MVC merupakan singkatan dari Model, View, Controller.
    Model bertugas untuk mengelola data pada database dan me-respond kepada request user.
    View bertugas untuk menangkap input dan menampilkan data tersebut kepada user.
    Controller bertugas untuk menghubungkan Model dan View. Controller menerima input dari View, memberikan nya ke Model, lalu mengganti View
    sesuai input tersebut.

    MVT merupakan singkatan dari Model, View, Template.
    Model pada MVT memiliki tugas yang mirip dengan Model pada MVC, yaitu untuk mengelola data.
    View bertanggung jawab untuk menerima web request dan memberikan response yang sesuai.
    Template bertugas untuk menampilkan data yang diterima dari View.

    MVVM merupakan singkatan dari Model, View, ViewModel.
    Model pada MVVM memiliki tugas yang mirip dengan Model pada MVC dan MVT, yaitu untuk mengelola data.
    View pada MVVM juga memiliki tugas yang mirip dengan View pada MVC dan MVT, yaitu berhubungan dengan User Interface.
    ViewModel bertugas untuk menghubungkan Model dan View dengan menerima data dari Model dan memberikannya ke View.

    Salah satu perbedaan dari MVC, MVT, dan MVVM adalah interaksi View nya. Pada MVC, View berhubungan dengan Controller untuk mengirimkan input
    user serta me-request update dari Model. Pada MVT, View menggunakan View functions untuk mengakses Model dan me-return HTTP response. Dan pada
    MVVM, View berinteraksi dengan ViewModel yang akan menghubungkan dengan Model.