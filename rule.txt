;;;======================================================
;;;   Shape Detection
;;;
;;;     This expert system diagnoses some simple
;;;     image with the chosen shape
;;;
;;;     CLIPS Version 6.3 Example
;;;
;;;======================================================

;;;***************
;;;* QUERY RULES *
;;;***************

(defrule determine-segitiga ""
    (total-point 3)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga")
    (assert (is segitiga)))

(defrule determine-segitiga-tumpul ""
    (is segitiga)
    (sudut utama atas 90)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-tumpul")
    (assert (is tumpul)))

(defrule determine-segitiga-tumpul-sama-kaki ""
    (is tumpul)
    (ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-tumpul-sama-kaki")
    (assert (bentuk "segitiga tumpul sama kaki")))

(defrule determine-segitiga-tumpul-tidak-beraturan ""
    (is tumpul)
    (tidak ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-tumpul-tidak-beraturan")
    (assert (bentuk "segitiga tumpul tidak beraturan")))

(defrule determine-segitiga-siku ""
    (is segitiga)
    (sudut utama sama 90)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-siku")
    (assert (is siku)))

(defrule determine-segitiga-siku-sama-kaki ""
    (is siku)
    (ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-siku-sama-kaki")
    (assert (bentuk "segitiga siku sama kaki")))

(defrule determine-segitiga-siku-tidak-beraturan ""
    (is siku)
    (tidak ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-siku-tidak-beraturan")
    (assert (bentuk "segitiga siku tidak beraturan")))

(defrule determine-segitiga-lancip ""
    (is segitiga)
    (sudut utama bawah 90)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-lancip")
    (assert (is lancip)))

(defrule determine-segitiga-lancip-sama-kaki ""
    (is lancip)
    (ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-lancip-sama-kaki")
    (assert (bentuk "segitiga lancip sama kaki")))

(defrule determine-segitiga-lancip-sama-sisi ""
    (is lancip)
    (semua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-lancip-sama-sisi")
    (assert (bentuk "segitiga sama sisi")))

(defrule determine-segitiga-lancip-tidak-beraturan ""
    (is lancip)
    (tidak ada dua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segitiga-lancip-tidak-beraturan")
    (assert (bentuk "segitiga lancip tidak beraturan")))

(defrule determine-segiempat ""
    (total-point 4)
    (not (bentuk ?))
    =>
    (callRule "determine-segiempat")
    (assert (is segiempat)))

(defrule determine-jajargenjang ""
    (is segiempat)
    (sisi 1 sama sisi 2)
    (sisi 3 sama sisi 4)
    (not (bentuk ?))
    =>
    (callRule "determine-jajargenjang")
    (assert (is jajargenjang)))

(defrule determine-layanglayang ""
    (is jajargenjang)
    (sudut 1 sama sudut 2)
    (sudut 3 tidak sama sudut 4)
    (not (bentuk ?))
    =>
    (callRule "determine-layanglayang")
    (assert (bentuk "layang-layang")))

(defrule determine-segi-empat-beraturan ""
    (semua sisi sama)
    (semua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segi-empat-beraturan")
    (assert (bentuk "segi empat beraturan")))

(defrule determine-trapesium ""
    (is segiempat)
    (sisi 1 sama sisi 2)
    (sisi 3 tidak sama sisi 4)
    (not (bentuk ?))
    =>
    (callRule "determine-trapesium")
    (assert (is trapesium)))

(defrule determine-trapesium-sama-kaki ""
    (is trapesium)
    (sudut 1 sama sudut 2)
    (sudut 3 sama sudut 4)
    (not (bentuk ?))
    =>
    (callRule "determine-trapesium-sama-kaki")
    (assert (bentuk "trapesium-sama-kaki")))

(defrule determine-trapesium-rata-kiri ""
    (is trapesium)
    (sudut 1 sama sudut 2)
    (sudut 1 sama 90)
    (not (bentuk ?))
    =>
    (callRule "determine-trapesium-rata-kiri")
    (assert (bentuk "trapesium-rata-kiri")))

(defrule determine-trapesium-rata-kanan ""
    (is trapesium)
    (sudut 3 sama sudut 4)
    (sudut 3 sama 90)
    (not (bentuk ?))
    =>
    (callRule "determine-trapesium-rata-kanan")
    (assert (bentuk "trapesium-rata-kanan")))

(defrule determine-segilima ""
    (total-point 5)
    (not (bentuk ?))
    =>
    (callRule "determine-segilima")
    (assert (is segilima)))

(defrule determine-segilima-sama-sisi ""
    (is segilima)
    (semua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segilima-sama-sisi")
    (assert (bentuk "segilima sama sisi")))

(defrule determine-segilima-tidak-beraturan ""
    (is segilima)
    (semua sudut tidak sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segilima-tidak-beraturan")
    (assert (bentuk "segilima tidak beraturan")))

(defrule determine-segienam ""
    (total-point 6)
    (not (bentuk ?))
    =>
    (callRule "determine-segienam")
    (assert (is segienam)))

(defrule determine-segienam-sama-sisi ""
    (is segienam)
    (semua sudut sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segienam-sama-sisi")
    (assert (bentuk "segienam sama sisi")))

(defrule determine-segienam-tidak-beraturan ""
    (is segienam)
    (semua sudut tidak sama)
    (not (bentuk ?))
    =>
    (callRule "determine-segienam-tidak-beraturan")
    (assert (bentuk "segienam tidak beraturan")))

;;;********************************
;;;* CONCLUSION RULES *
;;;********************************

(defrule judul-sistem ""
    (declare (salience 10))
    =>
    (printout t crlf)
    (printout t "Deteksi Bentuk"))

(defrule print-bentuk ""
    (declare (salience 10))
    (bentuk ?item)
    =>
    (printout t crlf)
    (printout t "Bentuk :")
    (format t " %s%n%n%n" ?item))