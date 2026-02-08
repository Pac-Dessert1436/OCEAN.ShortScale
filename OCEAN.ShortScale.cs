namespace OCEAN.ShortScale;

public enum OceanTrait : int
{
    Openness = 1,
    Conscientiousness = 2,
    Extraversion = 3,
    Agreeableness = 4,
    Neuroticism = 5
}

public record Question(string Text, OceanTrait Trait, bool IsReversed = false);

file static class Program
{
    public static void SaveResults(Dictionary<OceanTrait, double> averages)
    {
        string fileName = $"OCEAN_Results_{DateTime.Now:yyyyMMdd_HHmmss}.txt";

        try
        {
            using var file = new StreamWriter(fileName);
            file.WriteLine("OCEAN Personality Test Results");
            file.WriteLine($"Test Time: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");
            file.WriteLine(new string('-', 40));
            foreach (var kvp in averages)
                file.WriteLine($"{kvp.Key}: {kvp.Value:F2}/5.0");

            file.WriteLine(new string('-', 40));
            file.WriteLine("Trait Explanations:");
            file.WriteLine("Openness: High scores indicate imagination, curiosity, and openness to new experiences");
            file.WriteLine("Conscientiousness: High scores indicate organization, reliability, and self-discipline");
            file.WriteLine("Extraversion: High scores indicate social activity, energy, and positivity");
            file.WriteLine("Agreeableness: High scores indicate friendliness, cooperation, and compassion");
            file.WriteLine("Neuroticism: High scores indicate emotional sensitivity, anxiety, and tension");
            Console.WriteLine($"Results saved to: {fileName}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error saving file: {ex.Message}");
        }
    }

    internal static void Main()
    {
        Console.WriteLine("=== OCEAN Personality Short Scale Test ===\n");
        Console.WriteLine("Please rate the following statements on a scale of 1-5 according to your true feelings:");
        Console.WriteLine("(1 = Not at all, 2 = Slightly, 3 = Moderately, 4 = Quite well, 5 = Perfectly)");

        List<Question> questions =
        [
            // Openness - 8 questions
            new("I have a deep appreciation for art and beauty.", OceanTrait.Openness),
            new("I enjoy trying new and different things.", OceanTrait.Openness),
            new("I often have various creative ideas.", OceanTrait.Openness),
            new("I prefer routine over change.", OceanTrait.Openness, true),
            new("I enjoy exploring abstract philosophical concepts.", OceanTrait.Openness),
            new("I am curious about different cultures and lifestyles.", OceanTrait.Openness),
            new("I rarely think about the meaning and purpose of life.", OceanTrait.Openness, true),
            new("I enjoy appreciating complex music, literature, or artworks.", OceanTrait.Openness),

            // Conscientiousness - 8 questions
            new("I am always organized and planned in my work.", OceanTrait.Conscientiousness),
            new("I carefully complete all tasks assigned to me.", OceanTrait.Conscientiousness),
            new("I tend to be lazy and procrastinate.", OceanTrait.Conscientiousness, true),
            new("I am very careful and meticulous in my work.", OceanTrait.Conscientiousness),
            new("I set clear goals for the future and work hard to achieve them.", OceanTrait.Conscientiousness),
            new("I often forget to complete important things.", OceanTrait.Conscientiousness, true),
            new("I pay attention to details and strive to do things perfectly.", OceanTrait.Conscientiousness),
            new("I get easily distracted and have trouble focusing on long-term tasks.", OceanTrait.Conscientiousness, true),

            // Extraversion - 8 questions
            new("I like to be the center of attention in a group.", OceanTrait.Extraversion),
            new("I feel energetic and full of vitality.", OceanTrait.Extraversion),
            new("I always take the initiative to talk to people at social gatherings.", OceanTrait.Extraversion),
            new("I prefer being alone rather than participating in social activities.", OceanTrait.Extraversion, true),
            new("I enjoy participating in lively activities with others.", OceanTrait.Extraversion),
            new("I feel reserved and shy in front of strangers.", OceanTrait.Extraversion, true),
            new("I like to spend most of my time with friends.", OceanTrait.Extraversion),
            new("I gain energy and pleasure from social interactions.", OceanTrait.Extraversion),

            // Agreeableness - 8 questions
            new("I usually trust others.", OceanTrait.Agreeableness),
            new("I am willing to help others.", OceanTrait.Agreeableness),
            new("I tend to criticize or be picky about others.", OceanTrait.Agreeableness, true),
            new("I consider the feelings and needs of others.", OceanTrait.Agreeableness),
            new("I easily forgive others' mistakes.", OceanTrait.Agreeableness),
            new("I often have arguments or conflicts with others.", OceanTrait.Agreeableness, true),
            new("I am willing to make concessions for team harmony.", OceanTrait.Agreeableness),
            new("I feel empathy and sadness for others' misfortunes.", OceanTrait.Agreeableness),

            // Neuroticism - 8 questions
            new("I often feel anxious or nervous.", OceanTrait.Neuroticism),
            new("My emotions fluctuate quite a bit.", OceanTrait.Neuroticism),
            new("I can handle stress well.", OceanTrait.Neuroticism, true),
            new("I get easily annoyed by small things.", OceanTrait.Neuroticism),
            new("I often worry about possible bad things happening.", OceanTrait.Neuroticism),
            new("I can quickly calm down when facing setbacks.", OceanTrait.Neuroticism, true),
            new("I often feel depressed or in low spirits.", OceanTrait.Neuroticism),
            new("I am very sensitive to criticism and rejection.", OceanTrait.Neuroticism)
        ];

        // Initialize scores dictionary
        Dictionary<OceanTrait, List<int>> scores = [];
        foreach (OceanTrait trait in Enum.GetValues<OceanTrait>())
        {
            scores[trait] = [];
        }

        // Collect user responses
        for (int i = 0; i < questions.Count; i++)
        {
            Question quest = questions[i];

            while (true)
            {
                Console.WriteLine($"Question {i + 1}/{questions.Count}:");
                Console.WriteLine($"{quest.Text}");
                Console.Write("Please rate the question (1-5): ");

                string input = Console.ReadLine() ?? "";

                if (int.TryParse(input, out int score) && score >= 1 && score <= 5)
                {
                    // Handle reversed scoring questions
                    int finalScore = quest.IsReversed ? (6 - score) : score;
                    scores[quest.Trait].Add(finalScore);
                    Console.WriteLine();
                    break;
                }
                else
                {
                    Console.WriteLine("Please enter a number between 1 and 5.\n");
                }
            }
        }

        Console.WriteLine("\n" + new string('=', 50));
        Console.WriteLine("=== OCEAN Personality Short Scale Results ===\n");

        Dictionary<OceanTrait, double> averages = [];
        Dictionary<OceanTrait, string> interpretations = new()
        {
            { OceanTrait.Openness, "High: Imaginative, curious, creative; Low: Practical, traditional, conservative" },
            { OceanTrait.Conscientiousness, "High: Organized, reliable, disciplined; Low: Spontaneous, flexible, casual" },
            { OceanTrait.Extraversion, "High: Sociable, talkative, energetic; Low: Quiet, reserved, independent" },
            { OceanTrait.Agreeableness, "High: Friendly, compassionate, helpful; Low: Critical, competitive, skeptical" },
            { OceanTrait.Neuroticism, "High: Emotional, anxious, sensitive; Low: Emotionally stable, calm, resilient" }
        };

        foreach (OceanTrait trait in Enum.GetValues<OceanTrait>())
        {
            List<int> traitScores = scores[trait];
            double average = traitScores.Count > 0 ? traitScores.Average() : 0;
            averages[trait] = average;

            // 显示分数条
            int barLength = (int)(average * 8);
            string bar = new string('★', barLength) + new string('☆', 40 - barLength);

            Console.WriteLine($"{trait}: Average Score {average:F2}/5.0");
            Console.WriteLine($"  [{bar}]");

            // 提供简单解读
            string level = average switch
            {
                >= 4.0 => "Very high",
                >= 3.0 => "Moderately high",
                >= 2.0 => "Moderately low",
                _ => "Very low"
            };
            Console.WriteLine($"  ({level}) - {interpretations[trait]}");
            Console.WriteLine();
        }

        Console.WriteLine("\n" + new string('=', 50));
        Console.Write("Save results to file? (y/n): ");
        while (true)
        {
            string saveChoice = Console.ReadLine() ?? "";
            if (saveChoice?.ToLower() == "y")
            {
                SaveResults(averages);
                break;
            }
            else if (saveChoice?.ToLower() == "n")
            {
                Console.WriteLine("Save canceled.");
                break;
            }
            else
            {
                Console.Write("Invalid input. Please enter 'y' or 'n': ");
            }
        }

        Console.WriteLine("\nTest completed. Thank you for your participation!");
        Console.WriteLine("Note: The OCEAN personality traits describe general tendencies and are a good starting point for personal growth.");
        Console.WriteLine("      Every person's personality is unique and developable.");
    }
}