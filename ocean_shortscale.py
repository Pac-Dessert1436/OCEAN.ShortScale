import tkinter as tk
from tkinter import ttk, messagebox
from enum import IntEnum, unique
from dataclasses import dataclass
import datetime


@unique
class OceanTrait(IntEnum):
    Openness = 1
    Conscientiousness = 2
    Extraversion = 3
    Agreeableness = 4
    Neuroticism = 5


@dataclass
class Question:
    text: str
    trait: OceanTrait
    is_reversed: bool = False


class OceanTestApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("OCEAN Personality Test")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Set up styles
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("Title.TLabel", font=("Arial", 16, "bold"))
        self.style.configure("TButton", font=("Arial", 12))
        self.style.configure("Question.TLabel", font=("Arial", 14, "bold"))

        # Initialize variables
        self.questions = self._get_questions()
        self.current_question_index = 0
        self.scores = {trait: [] for trait in OceanTrait}
        self.averages = {}

        # Create main container
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Show welcome screen
        self._show_welcome_screen()

    def _get_questions(self) -> list[Question]:
        return [
            # Openness - 8 questions
            Question("I have a deep appreciation for art and beauty.",
                     OceanTrait.Openness),
            Question("I enjoy trying new and different things.",
                     OceanTrait.Openness),
            Question("I often have various creative ideas.",
                     OceanTrait.Openness),
            Question("I prefer routine over change.",
                     OceanTrait.Openness, True),
            Question("I enjoy exploring abstract philosophical concepts.",
                     OceanTrait.Openness),
            Question("I am curious about different cultures and lifestyles.",
                     OceanTrait.Openness),
            Question("I rarely think about the meaning and purpose of life.",
                     OceanTrait.Openness, True),
            Question("I enjoy appreciating complex music, literature, or artworks.",
                     OceanTrait.Openness),

            # Conscientiousness - 8 questions
            Question("I am always organized and planned in my work.",
                     OceanTrait.Conscientiousness),
            Question("I carefully complete all tasks assigned to me.",
                     OceanTrait.Conscientiousness),
            Question("I tend to be lazy and procrastinate.",
                     OceanTrait.Conscientiousness, True),
            Question("I am very careful and meticulous in my work.",
                     OceanTrait.Conscientiousness),
            Question("I set clear goals for the future and work hard to achieve them.",
                     OceanTrait.Conscientiousness),
            Question("I often forget to complete important things.",
                     OceanTrait.Conscientiousness, True),
            Question("I pay attention to details and strive to do things perfectly.",
                     OceanTrait.Conscientiousness),
            Question("I get easily distracted and have trouble focusing on long-term tasks.",
                     OceanTrait.Conscientiousness, True),

            # Extraversion - 8 questions
            Question("I like to be the center of attention in a group.",
                     OceanTrait.Extraversion),
            Question("I feel energetic and full of vitality.",
                     OceanTrait.Extraversion),
            Question("I always take the initiative to talk to people at social gatherings.",
                     OceanTrait.Extraversion),
            Question("I prefer being alone rather than participating in social activities.",
                     OceanTrait.Extraversion, True),
            Question("I enjoy participating in lively activities with others.",
                     OceanTrait.Extraversion),
            Question("I feel reserved and shy in front of strangers.",
                     OceanTrait.Extraversion, True),
            Question("I like to spend most of my time with friends.",
                     OceanTrait.Extraversion),
            Question("I gain energy and pleasure from social interactions.",
                     OceanTrait.Extraversion),

            # Agreeableness - 8 questions
            Question("I usually trust others.",
                     OceanTrait.Agreeableness),
            Question("I am willing to help others.",
                     OceanTrait.Agreeableness),
            Question("I tend to criticize or be picky about others.",
                     OceanTrait.Agreeableness, True),
            Question("I consider the feelings and needs of others.",
                     OceanTrait.Agreeableness),
            Question("I easily forgive others' mistakes.",
                     OceanTrait.Agreeableness),
            Question("I often have arguments or conflicts with others.",
                     OceanTrait.Agreeableness, True),
            Question("I am willing to make concessions for team harmony.",
                     OceanTrait.Agreeableness),
            Question("I feel empathy and sadness for others' misfortunes.",
                     OceanTrait.Agreeableness),

            # Neuroticism - 8 questions
            Question("I often feel anxious or nervous.",
                     OceanTrait.Neuroticism),
            Question("My emotions fluctuate quite a bit.",
                     OceanTrait.Neuroticism),
            Question("I can handle stress well.",
                     OceanTrait.Neuroticism, True),
            Question("I get easily annoyed by small things.",
                     OceanTrait.Neuroticism),
            Question("I often worry about possible bad things happening.",
                     OceanTrait.Neuroticism),
            Question("I can quickly calm down when facing setbacks.",
                     OceanTrait.Neuroticism, True),
            Question("I often feel depressed or in low spirits.",
                     OceanTrait.Neuroticism),
            Question("I am very sensitive to criticism and rejection.",
                     OceanTrait.Neuroticism)
        ]

    def _show_welcome_screen(self) -> None:
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Welcome title
        title_label = ttk.Label(
            self.main_frame, text="=== OCEAN Personality Short Scale Test ===", style="Title.TLabel")
        title_label.pack(pady=20)

        # Instructions
        instructions = ttk.Label(
            self.main_frame, text="Please rate the following statements on a scale of 1-5 according to your true feelings:", wraplength=700)
        instructions.pack(pady=10)

        rating_scale = ttk.Label(
            self.main_frame, text="(1 = Not at all, 2 = Slightly, 3 = Moderately, 4 = Quite well, 5 = Perfectly)")
        rating_scale.pack(pady=10)

        # Start button
        start_button = ttk.Button(
            self.main_frame, text="Start Test", command=self._show_next_question)
        start_button.pack(pady=30)

    def _show_next_question(self) -> None:
        if self.current_question_index >= len(self.questions):
            self._show_results()
            return

        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Get current question
        question = self.questions[self.current_question_index]

        # Question number
        question_number = ttk.Label(
            self.main_frame, text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
        question_number.pack(pady=10)

        # Question text
        question_text = ttk.Label(
            self.main_frame, text=question.text, style="Question.TLabel", wraplength=700)
        question_text.pack(pady=20)

        # Rating scale
        self.rating_var = tk.IntVar()
        rating_frame = ttk.Frame(self.main_frame)
        rating_frame.pack(pady=20)

        for i in range(1, 6):
            radio = ttk.Radiobutton(rating_frame, text=str(
                i), variable=self.rating_var, value=i)
            radio.pack(side=tk.LEFT, padx=20)

        # Navigation buttons
        nav_frame = ttk.Frame(self.main_frame)
        nav_frame.pack(pady=30)

        if self.current_question_index > 0:
            prev_button = ttk.Button(
                nav_frame, text="Previous", command=self._show_previous_question)
            prev_button.pack(side=tk.LEFT, padx=10)

        next_button = ttk.Button(
            nav_frame, text="Next", command=self._save_answer)
        next_button.pack(side=tk.RIGHT, padx=10)

    def _show_previous_question(self) -> None:
        if self.current_question_index > 0:
            self.current_question_index -= 1
            # Remove the last answer for this question
            question = self.questions[self.current_question_index]
            if self.scores[question.trait]:
                self.scores[question.trait].pop()
            self._show_next_question()

    def _save_answer(self) -> None:
        rating = self.rating_var.get()
        if rating == 0:
            messagebox.showwarning(
                "Warning", "Please select a rating from 1-5!")
            return

        # Get current question
        question = self.questions[self.current_question_index]

        # Handle reverse scoring
        final_score = 6 - rating if question.is_reversed else rating
        self.scores[question.trait].append(final_score)

        # Move to next question
        self.current_question_index += 1
        self._show_next_question()

    def _show_results(self) -> None:
        # Calculate averages
        self.averages = {}
        for trait in OceanTrait:
            if self.scores[trait]:
                self.averages[trait] = sum(
                    self.scores[trait]) / len(self.scores[trait])
            else:
                self.averages[trait] = 0

        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Results title
        results_title = ttk.Label(
            self.main_frame, text="=== OCEAN Personality Short Scale Results ===", style="Title.TLabel")
        results_title.pack(pady=20)

        # Results container
        results_frame = ttk.Frame(self.main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Interpretations
        interpretations = {
            OceanTrait.Openness: "High: Imaginative, curious, creative; Low: Practical, traditional, conservative",
            OceanTrait.Conscientiousness: "High: Organized, reliable, disciplined; Low: Spontaneous, flexible, casual",
            OceanTrait.Extraversion: "High: Sociable, talkative, energetic; Low: Quiet, reserved, independent",
            OceanTrait.Agreeableness: "High: Friendly, compassionate, helpful; Low: Critical, competitive, skeptical",
            OceanTrait.Neuroticism: "High: Emotional, anxious, sensitive; Low: Emotionally stable, calm, resilient"
        }

        # Display results
        for trait in OceanTrait:
            trait_frame = ttk.LabelFrame(
                results_frame, text=trait.name, padding="10")
            trait_frame.pack(fill=tk.X, pady=5)

            avg = self.averages[trait]
            avg_label = ttk.Label(
                trait_frame, text=f"Average Score: {avg:.2f}/5.0")
            avg_label.pack(anchor=tk.W, pady=5)

            # Progress bar
            progress_frame = ttk.Frame(trait_frame)
            progress_frame.pack(fill=tk.X, pady=5)

            # Text-based progress bar
            bar_length = int(avg * 8)
            bar = "★" * bar_length + "☆" * (40 - bar_length)
            bar_label = ttk.Label(progress_frame, text=f"[{bar}]")
            bar_label.pack(anchor=tk.W)

            # Level interpretation
            level = ""
            if avg >= 4.0:
                level = "Very High"
            elif avg >= 3.0:
                level = "Moderately High"
            elif avg >= 2.0:
                level = "Moderately Low"
            else:
                level = "Very Low"

            level_label = ttk.Label(
                trait_frame, text=f"({level}) - {interpretations[trait]}", wraplength=700)
            level_label.pack(anchor=tk.W, pady=5)

        # Save button
        save_button = ttk.Button(
            self.main_frame, text="Save Results", command=self._save_results)
        save_button.pack(pady=20)

        # Close button
        close_button = ttk.Button(
            self.main_frame, text="Close", command=self.root.quit)
        close_button.pack(pady=10)

        # Final message
        final_message = ttk.Label(
            self.main_frame, text="Note: The OCEAN personality traits describe general tendencies and are a good starting point for personal growth.", wraplength=700)
        final_message.pack(pady=10)

        final_message2 = ttk.Label(
            self.main_frame, text="Every person's personality is unique and developable.", wraplength=700)
        final_message2.pack(pady=5)

    def _save_results(self) -> None:
        try:
            # Create filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"OCEAN_Results_{timestamp}.txt"

            with open(filename, "w", encoding="utf-8") as file:
                file.write("OCEAN Personality Test Results\n")
                file.write(
                    f"Test Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("-" * 40 + "\n")

                for trait in OceanTrait:
                    file.write(
                        f"{trait.name}: {self.averages[trait]:.2f}/5.0\n")

                file.write("-" * 40 + "\n")
                file.write("Trait Explanations:\n")
                file.write(
                    "Openness: High scores indicate imagination, curiosity, and openness to new experiences\n")
                file.write(
                    "Conscientiousness: High scores indicate organization, reliability, and self-discipline\n")
                file.write(
                    "Extraversion: High scores indicate social activity, energy, and positivity\n")
                file.write(
                    "Agreeableness: High scores indicate friendliness, cooperation, and compassion\n")
                file.write(
                    "Neuroticism: High scores indicate emotional sensitivity, anxiety, and tension\n")

            messagebox.showinfo("Success", f"Results saved to: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save results: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = OceanTestApp(root)
    root.mainloop()
