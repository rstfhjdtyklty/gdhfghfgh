import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz - Typ Studenta")

        self.pytania = [
            "1. Dlaczego jesteś na tych studiach?",
            "2. Jak często wychodzisz ze znajomymi?",
            "3. Jak często prosisz o notatki z zajęć?",
            "4. Jak często poprawiasz kolokwia/egzaminy?",
            "5. Czy dobrze się uczysz?",
            "6. Kiedy zaczynasz naukę na zaliczenie?",
            "7. Jakie masz podejście do egzaminów na studiach?",
            "8. Jak często zdarzy ci się zasnąć na zajęciach?",
            "9. Jakie jest twoje podejście do pracy zespołowej?",
            "10. Jak reagujesz na trudności w nauce?",
            "11. Ilu zeszytów potrzebujesz?"
        ]

        self.odpowiedzi = [
            ["a) Aby mieć zniżki na PKP", "b) Bo nigdzie się nie dostałem/am", "c) Chcę dobrze zarabiać", "d) To moje powołanie"],
            ["a) Codziennie", "b) Raz w tygodniu", "c) Kilka razy w miesiącu", "d) Raz w semestrze"],
            ["a) Jakie notatki?", "b) Mój kolega pisze wszystko za mnie", "c) Tylko gdy sam nie mogłem/am być na zajęciach", "d) To ja wysyłam notatki innym"],
            ["a) Brakuje dla mnie terminów", "b) 3 terminy starczą", "c) Zdarzyło mi się raz/dwa", "d) Jeszcze nigdy nic nie musiałem/am poprawiać"],
            ["a) Nie", "b) Byleby zdać", "c) Wystarczająco dobrze", "d) Tak"],
            ["a) Nie uczę się", "b) Wieczór przed", "c) Tydzień przed", "d) Zaczynam już na początku semestru"],
            ["a) Wykorzystuję warunki i drugie terminy", "b) Nie uczę się, biorę na logikę", "c) Od tego zależy cała moja przyszłość", "d) Stawiam ją najwyżej w moich celach"],
            ["a) Pojawiam się i od razu zasypiam", "b) Jestem tylko człowiekiem", "c) Zdarzyło mi się raz", "d) Nigdy w życiu, zawsze uważnie słucham i notuję"],
            ["a) Zazwyczaj jestem bierny/a w projektach grupowych", "b) Robię najmniej", "c) Lubię współpracować z innymi i dzielić się pomysłami", "d) Wolę pracować samodzielnie, ale potrafię dostosować się do zespołu"],
            ["a) Czasami się zniechęcam i rezygnuję", "b) Wychodzę z założenia, że uda mi się ściągnąć", "c) Zazwyczaj ignoruję trudności, licząc na lepsze czasy", "d) Szukam dodatkowej pomocy, pytając nauczycieli lub kolegów"],
            ["a) Okrągłe zero", "b) Kartka i długopis starczą", "c) Jeden do wszystkiego", "d) Do każdego przedmiotu osobny"]
        ]

        self.punkty_typu_studenta = {
            "a": 1,
            "b": 2,
            "c": 3,
            "d": 4
        }

        self.suma_punktow = 0
        self.current_question = 0

        self.label_question = tk.Label(master, text=self.pytania[self.current_question], justify="left")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)  # Ustawienie początkowej wartości na None

        self.radio_buttons = []

        for odpowiedz in self.odpowiedzi[self.current_question]:
            radio_btn = tk.Radiobutton(master, text=odpowiedz, variable=self.radio_var, value=odpowiedz[0].lower())
            radio_btn.pack(anchor="w")
            self.radio_buttons.append(radio_btn)

        self.button_next = tk.Button(master, text="Następne", command=self.next_question)
        self.button_next.pack(side=tk.BOTTOM, pady=10)

    def next_question(self):
        selected_answer = self.radio_var.get()
        if selected_answer:
            self.suma_punktow += self.punkty_typu_studenta[selected_answer]
            self.current_question += 1

            if self.current_question < len(self.pytania):
                self.label_question.config(text=self.pytania[self.current_question])
                self.radio_var.set(None)  # Ustawienie wartości na None

                for radio_btn in self.radio_buttons:
                    radio_btn.destroy()
         
                self.radio_buttons = []
                for odpowiedz in self.odpowiedzi[self.current_question]:
                    radio_btn = tk.Radiobutton(self.master, text=odpowiedz, variable=self.radio_var,
                                               value=odpowiedz[0].lower())
                    radio_btn.pack(anchor="w")
                    self.radio_buttons.append(radio_btn)
            else:
                self.show_result()
        else:
            messagebox.showinfo("Błąd", "Wybierz odpowiedź.")

    def show_result(self):
        result_text = ""
        if 0 <= self.suma_punktow <= 11:
            result_text = "Typ: Turysta akademicki - Nigdy nie jesteś na nic przygotowany/a! Pojawiłeś/as się na uczelni tylko dla zniżek i spotkań ze znajomymi. Lepiej pomyśl nad swoim postępowaniem, ponieważ z obecnym nastawieniem długo nie pobędziesz studentem."
        elif 12 <= self.suma_punktow <= 21:
            result_text = "Typ: Mistrz Sztuki Utrzymywania Pozorów - Starasz się sprawiać pozory, że zależy Ci na nauce i studiach. Brakuje ci motywacji oraz samozaparcia. Jeszcze uda się to naprawić, musisz tylko chcieć! (Wierzymy w Ciebie)."
        elif 22 <= self.suma_punktow <= 32:
            result_text = "Typ: Guru Balansu - Szukasz równowagi między nauką, a życiem towarzyskim. Zdajesz sobie sprawę, że zamiast 4 mógłbyś/mogłabyś otrzymywać 5, ale wychodzisz z założenia 'Co dużo, to niezdrowo'."
        elif 33 <= self.suma_punktow <= 44:
            result_text = "Typ: Wzór do Naśladowania - Jesteś idealnym, zorganizowanym i systematycznym studentem. W Twoim indeksie znajdują się same 5. Stypendium gwarantowane! Takie zachowanie jak najbardziej na plus :D."

        messagebox.showinfo("Wynik quizu", result_text)
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()