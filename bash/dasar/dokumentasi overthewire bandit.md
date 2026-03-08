Haloooo

Pertama,ini cuman isi dari perintah yang pernah gw pelajari di overthewore level bandit 

lvel 0>1
kita hanya disuruh login remote ssh,sukup ``` ssh <nana>@<ip/domain overthewire> -p 2220 ```,dan hanya memakai ```cat * ``` untuk melihat isi file nya.
udah gitu aja,terus kita salin,dan ke level selanjutnya.

lvl 1>2
disini kita dilatih untuk melihat isi file dengan karakter unik,bukan alphabet biasa.
``` cat ./- ``` ,dan kita lagi lagi berhasil mendapatkan pw untuk level selanjutnya,bandit2.
btw,cat itu bisa dibilang perintah linux yang fungsi utamanya itu melihat isi dari sebuah file,tapi uniknya,disini kita
juga bisa membuat file baru dengan metode "Heredoc" loh.gini nih contoh nya
``` cat <<'EOF' > file_baru.sh ```
``` echo "Halo $USER" ```
``` EOF ```
  

