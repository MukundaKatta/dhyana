"""Library of meditation techniques."""

from typing import Optional

from dhyana.models import Technique, MeditationStyle, Difficulty


# 16 meditation techniques
TECHNIQUES: list[Technique] = [
    Technique(
        name="Vipassana (Insight Meditation)",
        style=MeditationStyle.VIPASSANA,
        description=(
            "One of the oldest Buddhist meditation practices, Vipassana means "
            "'to see things as they really are.' It involves systematic observation "
            "of body sensations to understand the impermanent nature of all phenomena."
        ),
        instructions=[
            "Sit comfortably with your spine straight and eyes closed.",
            "Begin by focusing on the natural breath at the nostrils.",
            "After settling the mind, systematically scan your body from head to toe.",
            "Observe any sensations that arise without reacting: tingling, warmth, pressure, pain.",
            "Maintain equanimity. Do not crave pleasant sensations or resist unpleasant ones.",
            "When the mind wanders, gently return to observing sensations.",
            "Continue scanning the body, moving attention methodically.",
        ],
        benefits=[
            "Develops deep self-awareness",
            "Reduces reactivity to stimuli",
            "Cultivates equanimity and inner peace",
            "Helps understand the impermanent nature of experience",
        ],
        difficulty=Difficulty.INTERMEDIATE,
        recommended_duration_minutes=20,
        origin="Ancient India, taught by Gotama Buddha, preserved in Theravada tradition",
        tips=[
            "Start with shorter sessions and gradually increase duration.",
            "Attend a 10-day retreat for proper instruction in the Goenka tradition.",
        ],
    ),
    Technique(
        name="Zazen (Seated Zen Meditation)",
        style=MeditationStyle.ZAZEN,
        description=(
            "The core meditation practice of Zen Buddhism. Zazen emphasizes "
            "'just sitting' (shikantaza) with alert awareness, letting thoughts "
            "arise and pass without engagement."
        ),
        instructions=[
            "Sit on a cushion (zafu) in full or half lotus position, or on a chair.",
            "Keep your spine straight, chin slightly tucked, eyes half-open gazing downward.",
            "Place your hands in the cosmic mudra: left hand on right, thumbs lightly touching.",
            "Breathe naturally through the nose. Do not control the breath.",
            "Let thoughts arise and pass like clouds. Do not follow or suppress them.",
            "Simply sit with complete presence. This is shikantaza: just sitting.",
            "If using a koan, hold the question gently in awareness without seeking an answer.",
        ],
        benefits=[
            "Develops profound stillness and clarity",
            "Cultivates non-attachment to thoughts",
            "Builds discipline and concentration",
            "Opens the path to insight (kensho or satori)",
        ],
        difficulty=Difficulty.INTERMEDIATE,
        recommended_duration_minutes=25,
        origin="Chinese Chan Buddhism, formalized in Japanese Zen tradition",
        tips=[
            "Posture is essential. Invest in a proper zafu and zabuton.",
            "Practice with a sangha (community) when possible.",
        ],
    ),
    Technique(
        name="Yoga Nidra (Yogic Sleep)",
        style=MeditationStyle.YOGA_NIDRA,
        description=(
            "A systematic method of inducing complete physical, mental, and emotional "
            "relaxation while maintaining awareness. Practiced lying down, it guides "
            "the practitioner through progressive states between waking and sleeping."
        ),
        instructions=[
            "Lie flat on your back in shavasana (corpse pose). Use a blanket if needed.",
            "Close your eyes and set a sankalpa (intention or resolve).",
            "Follow the rotation of consciousness through each body part as guided.",
            "Become aware of the breath without altering it.",
            "Explore pairs of opposite sensations: heavy/light, hot/cold.",
            "Visualize the guided imagery with detached awareness.",
            "Return to your sankalpa. Gently bring awareness back to the room.",
        ],
        benefits=[
            "Deep relaxation equivalent to several hours of sleep",
            "Reduces chronic stress and anxiety",
            "Improves sleep quality",
            "Accesses the subconscious for personal transformation",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=30,
        origin="Ancient tantric practice, systematized by Swami Satyananda Saraswati",
        tips=[
            "Use a guided recording for best results.",
            "Practice at the same time daily to build a routine.",
        ],
    ),
    Technique(
        name="Trataka (Candle Gazing)",
        style=MeditationStyle.TRATAKA,
        description=(
            "A yogic purification practice (shatkarma) involving steady, unblinking "
            "gazing at a single point, typically a candle flame. It develops concentration "
            "and is said to stimulate the ajna (third eye) chakra."
        ),
        instructions=[
            "Place a lit candle at eye level, about two feet away.",
            "Sit comfortably with a straight spine.",
            "Gaze steadily at the tip of the flame without blinking.",
            "Keep your gaze soft and relaxed. If tears come, let them flow.",
            "After 2-3 minutes, close your eyes and observe the afterimage.",
            "Focus on the afterimage at the point between your eyebrows.",
            "When the image fades, open your eyes and repeat.",
        ],
        benefits=[
            "Dramatically improves concentration",
            "Strengthens eye muscles",
            "Purifies the eyes (in yogic tradition)",
            "Develops willpower and mental steadiness",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=10,
        origin="Hatha Yoga tradition, described in the Hatha Yoga Pradipika",
        tips=[
            "Practice in a dark, draft-free room for a steady flame.",
            "Remove contact lenses before practicing.",
        ],
    ),
    Technique(
        name="Metta Bhavana (Loving-Kindness Meditation)",
        style=MeditationStyle.METTA,
        description=(
            "A practice of systematically developing unconditional love and goodwill "
            "toward all beings, starting with oneself and progressively expanding outward. "
            "One of the four Brahmaviharas (sublime attitudes) in Buddhist tradition."
        ),
        instructions=[
            "Sit comfortably and close your eyes. Take a few deep breaths.",
            "Begin by directing loving-kindness toward yourself. Silently repeat: "
            "'May I be happy. May I be healthy. May I be safe. May I live with ease.'",
            "Bring to mind someone you love. Direct the same wishes toward them.",
            "Think of a neutral person (an acquaintance). Extend metta to them.",
            "Bring to mind a difficult person. With courage, extend metta to them too.",
            "Finally, extend loving-kindness to all beings everywhere.",
            "Rest in the feeling of boundless, unconditional goodwill.",
        ],
        benefits=[
            "Increases positive emotions and empathy",
            "Reduces self-criticism and negative self-talk",
            "Improves relationships and social connection",
            "Shown by research to increase vagal tone and well-being",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Theravada Buddhist tradition, taught by the Buddha in the Metta Sutta",
        tips=[
            "If you struggle with self-directed metta, start with a beloved pet or child.",
            "The phrases can be adapted to whatever resonates with you.",
        ],
    ),
    Technique(
        name="Breath Awareness (Anapanasati)",
        style=MeditationStyle.BREATH_AWARENESS,
        description=(
            "Mindfulness of breathing, one of the most fundamental meditation practices. "
            "The practitioner simply observes the natural breath without controlling it, "
            "using it as an anchor for present-moment awareness."
        ),
        instructions=[
            "Sit in a comfortable, stable position with your spine upright.",
            "Close your eyes or lower your gaze softly.",
            "Bring your attention to the natural flow of breathing.",
            "Notice the breath at the nostrils, chest, or abdomen - wherever it is most vivid.",
            "Observe the full cycle: inhalation, pause, exhalation, pause.",
            "When the mind wanders, gently note 'thinking' and return to the breath.",
            "There is no need to breathe in any special way. Simply observe.",
        ],
        benefits=[
            "Calms the nervous system",
            "Develops concentration and focus",
            "Reduces anxiety and stress",
            "Provides a reliable anchor for daily mindfulness",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=10,
        origin="Universal practice, central to Buddhist Anapanasati Sutta",
    ),
    Technique(
        name="Body Scan Meditation",
        style=MeditationStyle.BODY_SCAN,
        description=(
            "A systematic practice of bringing mindful attention to each part of "
            "the body in sequence. Popularized in Western mindfulness by Jon Kabat-Zinn "
            "as part of Mindfulness-Based Stress Reduction (MBSR)."
        ),
        instructions=[
            "Lie down or sit comfortably. Close your eyes.",
            "Bring awareness to your feet. Notice any sensations without judgment.",
            "Slowly move attention upward: ankles, calves, knees, thighs.",
            "Continue to the hips, lower back, abdomen, chest.",
            "Scan the hands, arms, shoulders, neck, face, and crown of the head.",
            "If you find tension, breathe into that area and allow it to soften.",
            "After scanning the entire body, rest in whole-body awareness.",
        ],
        benefits=[
            "Releases physical tension and chronic pain",
            "Develops interoception (body awareness)",
            "Reduces stress and promotes relaxation",
            "Improves mind-body connection",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Adapted from Burmese Vipassana, popularized in MBSR",
    ),
    Technique(
        name="Visualization Meditation",
        style=MeditationStyle.VISUALIZATION,
        description=(
            "Using the power of mental imagery to create inner experiences of peace, "
            "healing, or transformation. The practitioner vividly imagines specific "
            "scenes, colors, or scenarios that promote well-being."
        ),
        instructions=[
            "Sit or lie comfortably. Close your eyes and take several deep breaths.",
            "Begin to visualize a place where you feel completely safe and at peace.",
            "Engage all senses: see the colors, hear the sounds, feel the textures.",
            "Allow this place to become vivid and real in your mind's eye.",
            "Rest in this sanctuary. Let healing and peace flow through you.",
            "You may visualize light filling your body, warmth spreading, or roots grounding you.",
            "When ready, slowly let the image fade and return to present awareness.",
        ],
        benefits=[
            "Reduces anxiety through mental rehearsal",
            "Enhances creativity and problem-solving",
            "Supports healing and immune function",
            "Builds mental resilience",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Found across traditions: Tibetan Buddhism, Hindu Tantra, modern psychology",
    ),
    Technique(
        name="Mantra Meditation",
        style=MeditationStyle.MANTRA,
        description=(
            "Repetition of a sacred word, phrase, or sound to focus the mind and "
            "access deeper states of consciousness. The vibration of the mantra "
            "is believed to have transformative power."
        ),
        instructions=[
            "Choose a mantra. Classic options: Om, So Hum, Om Mani Padme Hum.",
            "Sit comfortably with your spine straight and eyes closed.",
            "Begin repeating the mantra silently in your mind.",
            "Synchronize the mantra with your breath if it feels natural.",
            "Let the repetition become effortless, almost as if the mantra repeats itself.",
            "When the mind wanders, gently return to the mantra.",
            "After the session, sit quietly for a few minutes before opening your eyes.",
        ],
        benefits=[
            "Provides a powerful focus point for the mind",
            "Creates calming vibrations in body and mind",
            "Accessible to beginners who struggle with silence",
            "Can induce deep meditative states",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=20,
        origin="Vedic tradition, used across Hinduism, Buddhism, Jainism, and Sikhism",
    ),
    Technique(
        name="Mindfulness Meditation (MBSR)",
        style=MeditationStyle.MINDFULNESS,
        description=(
            "Non-judgmental, present-moment awareness of thoughts, feelings, and "
            "sensations. Developed by Jon Kabat-Zinn, it is the foundation of "
            "Mindfulness-Based Stress Reduction, one of the most researched meditation methods."
        ),
        instructions=[
            "Sit in a comfortable position. You may close your eyes or keep them softly open.",
            "Bring attention to the present moment. Notice what is happening right now.",
            "Observe your breath, body sensations, thoughts, and emotions.",
            "When you notice a thought, label it gently: 'thinking,' 'planning,' 'remembering.'",
            "Return your attention to the present without judgment.",
            "Notice the tendency to resist unpleasant experiences or cling to pleasant ones.",
            "Practice accepting whatever arises with curiosity and kindness.",
        ],
        benefits=[
            "Clinically proven to reduce stress, anxiety, and depression",
            "Improves emotional regulation",
            "Enhances attention and cognitive flexibility",
            "Reduces rumination",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Adapted from Buddhist mindfulness by Jon Kabat-Zinn (1979)",
    ),
    Technique(
        name="Walking Meditation (Kinhin)",
        style=MeditationStyle.WALKING,
        description=(
            "A practice of bringing meditative awareness to the act of walking. "
            "Each step becomes an object of mindfulness, bridging formal sitting "
            "practice and daily life."
        ),
        instructions=[
            "Choose a path of 10-20 paces. Stand at one end with awareness.",
            "Begin walking very slowly. Feel each component: lifting, moving, placing.",
            "Coordinate awareness with each phase of the step.",
            "Keep your gaze soft, directed a few feet ahead on the ground.",
            "At the end of the path, pause, turn mindfully, and walk back.",
            "If the mind wanders, stop, re-center, and continue.",
            "Gradually you may walk at a normal pace while maintaining awareness.",
        ],
        benefits=[
            "Integrates mindfulness into movement",
            "Good for those who find sitting uncomfortable",
            "Develops body awareness and balance",
            "Bridges meditation and daily activities",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Theravada Buddhism (walking meditation) and Zen tradition (kinhin)",
    ),
    Technique(
        name="Transcendental Meditation Style",
        style=MeditationStyle.TRANSCENDENTAL,
        description=(
            "A technique involving the effortless use of a personally assigned mantra "
            "to settle the mind inward beyond thought to experience pure awareness. "
            "Practiced twice daily for 20 minutes."
        ),
        instructions=[
            "Sit comfortably with your eyes closed.",
            "Begin thinking your chosen mantra gently, without effort or concentration.",
            "Allow the mantra to become subtler and subtler.",
            "If you notice you have stopped thinking the mantra, gently return to it.",
            "The mantra may change or disappear as the mind settles. This is natural.",
            "After 20 minutes, stop the mantra and sit quietly for 2-3 minutes.",
            "Open your eyes slowly.",
        ],
        benefits=[
            "Reduces stress hormones (cortisol)",
            "Promotes deep rest and recovery",
            "Extensively researched with positive health outcomes",
            "Improves cardiovascular health markers",
        ],
        difficulty=Difficulty.INTERMEDIATE,
        recommended_duration_minutes=20,
        origin="Vedic tradition, popularized by Maharishi Mahesh Yogi (1958)",
    ),
    Technique(
        name="Chakra Meditation",
        style=MeditationStyle.CHAKRA,
        description=(
            "Meditation focused on the seven primary energy centers (chakras) "
            "along the spine. Each chakra is associated with specific qualities, "
            "colors, and aspects of consciousness."
        ),
        instructions=[
            "Sit comfortably with a straight spine. Close your eyes.",
            "Begin at the root chakra (base of spine). Visualize a red sphere of energy.",
            "Move to the sacral chakra (below navel). Visualize orange energy.",
            "Rise to the solar plexus (stomach area). Visualize golden yellow light.",
            "Bring attention to the heart chakra. Visualize green or pink light.",
            "Move to the throat chakra. Visualize blue light.",
            "Rise to the third eye (between eyebrows). Visualize indigo light.",
            "Finally, focus on the crown chakra (top of head). Visualize violet or white light.",
            "Feel all seven centers connected and aligned in a column of light.",
        ],
        benefits=[
            "Promotes energetic balance and alignment",
            "Develops subtle body awareness",
            "Can release energetic blockages",
            "Supports emotional and physical healing",
        ],
        difficulty=Difficulty.INTERMEDIATE,
        recommended_duration_minutes=20,
        origin="Hindu and Tantric yoga traditions",
    ),
    Technique(
        name="Sound Meditation (Nada Yoga)",
        style=MeditationStyle.SOUND,
        description=(
            "Using sound as the object of meditation, whether external (singing bowls, "
            "gongs, music) or internal (the inner sounds heard in deep silence). "
            "Nada Yoga is the yoga of inner sound."
        ),
        instructions=[
            "Sit comfortably in a quiet space. Close your eyes.",
            "Begin by listening to all the sounds in your environment without labeling them.",
            "Let sounds come and go without grasping or rejecting any of them.",
            "Gradually turn attention inward. Listen for subtler sounds within silence.",
            "You may hear a gentle ringing, humming, or buzzing. This is the nada.",
            "Focus on this inner sound and let it carry you deeper.",
            "Rest in pure listening, without any effort to hear anything specific.",
        ],
        benefits=[
            "Develops deep listening and receptivity",
            "Calms the mind through auditory focus",
            "Reduces tinnitus symptoms in some practitioners",
            "Opens awareness to subtle dimensions of experience",
        ],
        difficulty=Difficulty.INTERMEDIATE,
        recommended_duration_minutes=15,
        origin="Nada Yoga tradition, described in Hatha Yoga Pradipika",
    ),
    Technique(
        name="Open Awareness (Choiceless Awareness)",
        style=MeditationStyle.OPEN_AWARENESS,
        description=(
            "Rather than focusing on a single object, the practitioner rests in "
            "spacious awareness itself, allowing all experiences to arise and pass "
            "without preference. Associated with Dzogchen, Mahamudra, and J. Krishnamurti."
        ),
        instructions=[
            "Sit comfortably. Begin with a few minutes of breath awareness to settle.",
            "Gradually release the focus on breathing.",
            "Open your awareness to include everything: sounds, sensations, thoughts, emotions.",
            "Do not choose one object over another. Let awareness be panoramic.",
            "Notice the space in which all experiences arise.",
            "Rest as awareness itself, rather than being identified with any content.",
            "If you feel lost, briefly return to the breath, then open again.",
        ],
        benefits=[
            "Develops non-dual awareness",
            "Cultivates profound equanimity",
            "Integrates all experiences into meditation",
            "Deepens insight into the nature of mind",
        ],
        difficulty=Difficulty.ADVANCED,
        recommended_duration_minutes=20,
        origin="Dzogchen (Tibetan Buddhism), Mahamudra, and non-dual traditions",
    ),
    Technique(
        name="Loving-Kindness Visualization",
        style=MeditationStyle.LOVING_KINDNESS,
        description=(
            "Combines loving-kindness phrases with visualization, imagining warmth "
            "and light radiating from your heart to others. A more embodied approach "
            "to cultivating compassion and goodwill."
        ),
        instructions=[
            "Sit comfortably and bring attention to the center of your chest.",
            "Visualize a warm, golden light glowing in your heart area.",
            "As you breathe in, the light grows brighter. As you breathe out, it radiates outward.",
            "Bring yourself to mind. See the light surrounding you as you repeat: "
            "'May I be happy, may I be at peace.'",
            "Bring a loved one to mind. See the light reaching them.",
            "Expand the light to include acquaintances, then difficult people, then all beings.",
            "Rest in the feeling of boundless warmth and compassion.",
        ],
        benefits=[
            "Combines emotional and visual meditation for deeper impact",
            "Builds genuine compassion and empathy",
            "Reduces feelings of isolation and resentment",
            "Promotes emotional healing",
        ],
        difficulty=Difficulty.BEGINNER,
        recommended_duration_minutes=15,
        origin="Buddhist metta practice combined with visualization elements",
    ),
]


class TechniqueLibrary:
    """Library of meditation techniques with search and filtering."""

    def __init__(self) -> None:
        self._techniques = list(TECHNIQUES)

    @property
    def techniques(self) -> list[Technique]:
        """Return all techniques."""
        return list(self._techniques)

    @property
    def count(self) -> int:
        """Return the number of techniques."""
        return len(self._techniques)

    def get_by_style(self, style: MeditationStyle) -> Optional[Technique]:
        """Get a technique by its meditation style."""
        for tech in self._techniques:
            if tech.style == style:
                return tech
        return None

    def get_by_difficulty(self, difficulty: Difficulty) -> list[Technique]:
        """Get techniques filtered by difficulty level."""
        return [t for t in self._techniques if t.difficulty == difficulty]

    def get_by_name(self, name: str) -> Optional[Technique]:
        """Search for a technique by name (case-insensitive partial match)."""
        name_lower = name.lower()
        for tech in self._techniques:
            if name_lower in tech.name.lower():
                return tech
        return None

    def get_beginner_techniques(self) -> list[Technique]:
        """Get all beginner-friendly techniques."""
        return self.get_by_difficulty(Difficulty.BEGINNER)

    def get_for_duration(self, max_minutes: int) -> list[Technique]:
        """Get techniques that fit within a time constraint."""
        return [
            t for t in self._techniques
            if t.recommended_duration_minutes <= max_minutes
        ]

    def search(self, query: str) -> list[Technique]:
        """Search techniques by name, description, or benefits."""
        query_lower = query.lower()
        results = []
        for tech in self._techniques:
            searchable = (
                tech.name.lower()
                + " " + tech.description.lower()
                + " " + " ".join(b.lower() for b in tech.benefits)
            )
            if query_lower in searchable:
                results.append(tech)
        return results

    def get_recommended(self, mood: str) -> list[Technique]:
        """Get technique recommendations based on current mood."""
        mood_lower = mood.lower()
        if mood_lower in ("stressed", "anxious", "very_stressed", "tense"):
            styles = [
                MeditationStyle.BREATH_AWARENESS,
                MeditationStyle.BODY_SCAN,
                MeditationStyle.YOGA_NIDRA,
            ]
        elif mood_lower in ("sad", "lonely", "depressed"):
            styles = [
                MeditationStyle.METTA,
                MeditationStyle.LOVING_KINDNESS,
                MeditationStyle.MANTRA,
            ]
        elif mood_lower in ("scattered", "unfocused", "restless"):
            styles = [
                MeditationStyle.ZAZEN,
                MeditationStyle.TRATAKA,
                MeditationStyle.BREATH_AWARENESS,
            ]
        elif mood_lower in ("calm", "peaceful", "centered"):
            styles = [
                MeditationStyle.VIPASSANA,
                MeditationStyle.OPEN_AWARENESS,
                MeditationStyle.ZAZEN,
            ]
        else:
            styles = [
                MeditationStyle.MINDFULNESS,
                MeditationStyle.BREATH_AWARENESS,
                MeditationStyle.BODY_SCAN,
            ]
        return [t for t in self._techniques if t.style in styles]

    def add_technique(self, technique: Technique) -> None:
        """Add a custom technique to the library."""
        self._techniques.append(technique)
