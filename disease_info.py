# =============================================================
# Disease Info Database - Updated with correct class names
# File: disease_info.py
# =============================================================

DISEASE_INFO = {

    # ============ PEPPER ============
    "Pepper__bell___Bacterial_spot": {
        "en": {
            "name": "Pepper Bacterial Spot",
            "description": "Caused by Xanthomonas bacteria. Creates small, water-soaked spots on leaves that turn brown with yellow halos. Spreads rapidly in warm, wet weather.",
            "treatment": [
                "Apply copper-based bactericides immediately.",
                "Remove and destroy infected plant parts.",
                "Avoid overhead irrigation — use drip irrigation.",
                "Apply mancozeb + copper hydroxide spray every 7 days.",
                "Rotate crops — avoid planting peppers in same location."
            ],
            "severity": "High",
            "prevention": "Use disease-free certified seeds. Avoid working in wet fields."
        },
        "hi": {
            "name": "मिर्च का जीवाणु धब्बा रोग",
            "description": "Xanthomonas जीवाणु से होता है। पत्तियों पर पानी भरे धब्बे बनते हैं जो भूरे हो जाते हैं।",
            "treatment": [
                "तुरंत कॉपर आधारित जीवाणुनाशक लगाएं।",
                "संक्रमित हिस्सों को हटाकर नष्ट करें।",
                "ड्रिप सिंचाई का उपयोग करें।",
                "हर 7 दिन mancozeb + कॉपर का छिड़काव करें।"
            ],
            "severity": "अधिक",
            "prevention": "प्रमाणित बीजों का उपयोग करें।"
        }
    },

    "Pepper__bell___healthy": {
        "en": {
            "name": "Healthy Bell Pepper",
            "description": "Your bell pepper plant is healthy! No disease detected.",
            "treatment": [
                "Continue regular watering and fertilization.",
                "Monitor weekly for any signs of disease.",
                "Ensure good air circulation around plants."
            ],
            "severity": "None",
            "prevention": "Rotate crops seasonally. Use balanced fertilizers."
        },
        "hi": {
            "name": "स्वस्थ शिमला मिर्च",
            "description": "आपकी शिमला मिर्च स्वस्थ है! कोई रोग नहीं।",
            "treatment": ["नियमित देखभाल जारी रखें।", "साप्ताहिक निगरानी करें।"],
            "severity": "कोई नहीं",
            "prevention": "फसल चक्र अपनाएं।"
        }
    },

    # ============ POTATO ============
    "Potato___Early_blight": {
        "en": {
            "name": "Potato Early Blight",
            "description": "Caused by Alternaria solani. Dark brown spots with concentric rings appear on older leaves first. Reduces photosynthesis and yield significantly.",
            "treatment": [
                "Apply mancozeb or chlorothalonil fungicide every 7-10 days.",
                "Ensure adequate potassium fertilization.",
                "Remove severely infected leaves.",
                "Harvest at right time — don't leave tubers in ground too long."
            ],
            "severity": "Moderate",
            "prevention": "Use certified seed potatoes. Avoid overhead irrigation."
        },
        "hi": {
            "name": "आलू का प्रारंभिक झुलसा",
            "description": "Alternaria solani से होता है। पुरानी पत्तियों पर गोल भूरे धब्बे बनते हैं।",
            "treatment": [
                "7-10 दिन के अंतराल पर mancozeb का छिड़काव करें।",
                "पर्याप्त पोटेशियम उर्वरक दें।",
                "गंभीर रूप से संक्रमित पत्तियां हटाएं।"
            ],
            "severity": "मध्यम",
            "prevention": "प्रमाणित बीज आलू का उपयोग करें।"
        }
    },

    "Potato___Late_blight": {
        "en": {
            "name": "Potato Late Blight",
            "description": "Caused by Phytophthora infestans. Creates dark, water-soaked lesions. Spreads extremely fast in cool, moist weather. Same pathogen as Irish Potato Famine.",
            "treatment": [
                "Apply copper fungicides or metalaxyl-mancozeb combination.",
                "Destroy infected plant material — do NOT compost it.",
                "Harvest tubers early if disease is severe.",
                "Apply preventive fungicide sprays in humid weather.",
                "Ensure good field drainage."
            ],
            "severity": "Critical",
            "prevention": "Plant resistant varieties. Avoid fields with poor drainage."
        },
        "hi": {
            "name": "आलू का पछेती झुलसा",
            "description": "Phytophthora infestans से होता है। पत्तियों पर गहरे, पानी भरे धब्बे पड़ते हैं।",
            "treatment": [
                "कॉपर फफूंदनाशक या metalaxyl-mancozeb का प्रयोग करें।",
                "संक्रमित पौधों को जलाकर नष्ट करें।",
                "गंभीर संक्रमण में जल्दी कटाई करें।"
            ],
            "severity": "गंभीर",
            "prevention": "रोग-प्रतिरोधी किस्में लगाएं।"
        }
    },

    "Potato___healthy": {
        "en": {
            "name": "Healthy Potato",
            "description": "Your potato plant is healthy! No disease detected.",
            "treatment": [
                "Continue regular care.",
                "Ensure hilling is done properly.",
                "Monitor for Colorado potato beetle."
            ],
            "severity": "None",
            "prevention": "Use certified seed potatoes. Rotate crops every season."
        },
        "hi": {
            "name": "स्वस्थ आलू का पौधा",
            "description": "आपका आलू का पौधा स्वस्थ है!",
            "treatment": ["नियमित देखभाल करें।"],
            "severity": "कोई नहीं",
            "prevention": "प्रमाणित बीज आलू उपयोग करें।"
        }
    },

    # ============ TOMATO ============
    "Tomato_Bacterial_spot": {
        "en": {
            "name": "Tomato Bacterial Spot",
            "description": "Caused by Xanthomonas bacteria. Small, dark, water-soaked spots appear on leaves, stems, and fruits. Spreads rapidly in warm, wet conditions.",
            "treatment": [
                "Apply copper-based bactericides every 7-10 days.",
                "Remove infected plant debris immediately.",
                "Avoid overhead watering.",
                "Use disease-free transplants.",
                "Rotate crops every season."
            ],
            "severity": "High",
            "prevention": "Use resistant varieties. Avoid working in wet fields."
        },
        "hi": {
            "name": "टमाटर का जीवाणु धब्बा",
            "description": "Xanthomonas जीवाणु से होता है। पत्तियों पर छोटे काले धब्बे बनते हैं।",
            "treatment": [
                "कॉपर आधारित जीवाणुनाशक का छिड़काव करें।",
                "संक्रमित अवशेष हटाएं।",
                "ऊपर से पानी देने से बचें।"
            ],
            "severity": "अधिक",
            "prevention": "रोग-प्रतिरोधी किस्में लगाएं।"
        }
    },

    "Tomato_Early_blight": {
        "en": {
            "name": "Tomato Early Blight",
            "description": "Caused by Alternaria solani fungus. Appears as dark brown circular spots with concentric rings (target-board pattern) on older leaves first.",
            "treatment": [
                "Apply chlorothalonil, mancozeb, or copper fungicides.",
                "Remove lower infected leaves to slow disease spread.",
                "Stake plants to improve air circulation.",
                "Maintain adequate plant nutrition — potassium reduces severity.",
                "Rotate crops — don't plant tomatoes in same location yearly."
            ],
            "severity": "Moderate",
            "prevention": "Mulch around plants to prevent soil splash. Water at base of plant."
        },
        "hi": {
            "name": "टमाटर का अगेती झुलसा",
            "description": "Alternaria solani कवक से होता है। पुरानी पत्तियों पर गोल भूरे धब्बे बनते हैं।",
            "treatment": [
                "chlorothalonil, mancozeb या कॉपर फफूंदनाशक लगाएं।",
                "नीचे की संक्रमित पत्तियां हटाएं।",
                "पौधों को सहारा दें।"
            ],
            "severity": "मध्यम",
            "prevention": "पौधों के आसपास मल्च लगाएं।"
        }
    },

    "Tomato_Late_blight": {
        "en": {
            "name": "Tomato Late Blight",
            "description": "Caused by Phytophthora infestans. One of the most destructive tomato diseases. Creates dark water-soaked lesions on leaves and fruits.",
            "treatment": [
                "Apply copper-based fungicides or chlorothalonil immediately.",
                "Remove and destroy all infected plant parts.",
                "Avoid wetting foliage when watering — use drip irrigation.",
                "Apply preventive sprays of mancozeb every 5-7 days in humid weather.",
                "Destroy severely infected plants to prevent spread."
            ],
            "severity": "Critical",
            "prevention": "Use certified disease-free seeds. Plant in well-ventilated areas."
        },
        "hi": {
            "name": "टमाटर का पछेती झुलसा",
            "description": "Phytophthora infestans से होने वाला यह रोग सबसे विनाशकारी है।",
            "treatment": [
                "तुरंत कॉपर आधारित फफूंदनाशक लगाएं।",
                "संक्रमित हिस्सों को नष्ट करें।",
                "ड्रिप सिंचाई का उपयोग करें।"
            ],
            "severity": "गंभीर",
            "prevention": "प्रमाणित बीज उपयोग करें।"
        }
    },

    "Tomato_Leaf_Mold": {
        "en": {
            "name": "Tomato Leaf Mold",
            "description": "Caused by Passalora fulva fungus. Yellow patches appear on upper leaf surface with olive-green mold on the underside. Common in greenhouses.",
            "treatment": [
                "Improve air circulation in greenhouse.",
                "Apply fungicides like chlorothalonil or mancozeb.",
                "Reduce humidity below 85%.",
                "Remove infected leaves immediately.",
                "Use resistant tomato varieties."
            ],
            "severity": "Moderate",
            "prevention": "Maintain low humidity. Avoid wetting leaves."
        },
        "hi": {
            "name": "टमाटर का पत्ती फफूंद",
            "description": "Passalora fulva कवक से होता है। पत्तियों के ऊपर पीले धब्बे और नीचे जैतून-हरे रंग की फफूंद बनती है।",
            "treatment": [
                "हवा का प्रवाह बेहतर करें।",
                "chlorothalonil या mancozeb का छिड़काव करें।",
                "नमी 85% से कम रखें।"
            ],
            "severity": "मध्यम",
            "prevention": "कम नमी बनाए रखें।"
        }
    },

    "Tomato_Septoria_leaf_spot": {
        "en": {
            "name": "Tomato Septoria Leaf Spot",
            "description": "Caused by Septoria lycopersici fungus. Small circular spots with dark borders and light centers appear on lower leaves first.",
            "treatment": [
                "Apply chlorothalonil or mancozeb fungicides.",
                "Remove infected lower leaves immediately.",
                "Avoid overhead irrigation.",
                "Stake plants for better air circulation.",
                "Rotate crops every 2-3 years."
            ],
            "severity": "Moderate",
            "prevention": "Mulch soil surface. Remove plant debris after harvest."
        },
        "hi": {
            "name": "टमाटर का सेप्टोरिया पत्ती धब्बा",
            "description": "Septoria lycopersici से होता है। नीचे की पत्तियों पर छोटे गोल धब्बे बनते हैं।",
            "treatment": [
                "chlorothalonil या mancozeb का छिड़काव करें।",
                "संक्रमित पत्तियां हटाएं।",
                "ऊपर से पानी न दें।"
            ],
            "severity": "मध्यम",
            "prevention": "मिट्टी में मल्च लगाएं।"
        }
    },

    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "en": {
            "name": "Tomato Spider Mites",
            "description": "Caused by Tetranychus urticae (Two-spotted spider mite). Creates yellow stippling on leaves with fine webbing on undersides. Thrives in hot, dry conditions.",
            "treatment": [
                "Apply miticides like abamectin or bifenazate.",
                "Spray plants with strong water jets to dislodge mites.",
                "Apply neem oil spray every 5-7 days.",
                "Introduce predatory mites as biological control.",
                "Increase humidity around plants."
            ],
            "severity": "High",
            "prevention": "Avoid water stress. Monitor plants regularly in hot weather."
        },
        "hi": {
            "name": "टमाटर की मकड़ी घुन",
            "description": "Tetranychus urticae से होता है। पत्तियों पर पीले धब्बे और नीचे जाले बनते हैं।",
            "treatment": [
                "abamectin miticide का प्रयोग करें।",
                "तेज पानी से पौधे धोएं।",
                "नीम तेल का छिड़काव करें।"
            ],
            "severity": "अधिक",
            "prevention": "पानी की कमी न होने दें।"
        }
    },

    "Tomato__Target_Spot": {
        "en": {
            "name": "Tomato Target Spot",
            "description": "Caused by Corynespora cassiicola fungus. Creates circular brown lesions with concentric rings resembling a target on leaves.",
            "treatment": [
                "Apply azoxystrobin or chlorothalonil fungicides.",
                "Remove infected plant material.",
                "Improve air circulation by pruning.",
                "Avoid overhead irrigation.",
                "Apply fungicide preventively in humid weather."
            ],
            "severity": "Moderate",
            "prevention": "Stake plants properly. Avoid dense planting."
        },
        "hi": {
            "name": "टमाटर का लक्ष्य धब्बा",
            "description": "Corynespora cassiicola से होता है। पत्तियों पर निशाने जैसे गोल भूरे धब्बे बनते हैं।",
            "treatment": [
                "azoxystrobin फफूंदनाशक का प्रयोग करें।",
                "संक्रमित अवशेष हटाएं।",
                "छंटाई करके हवा प्रवाह बेहतर करें।"
            ],
            "severity": "मध्यम",
            "prevention": "पौधों को सहारा दें।"
        }
    },

    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "en": {
            "name": "Tomato Yellow Leaf Curl Virus",
            "description": "A viral disease spread by whiteflies (Bemisia tabaci). Causes severe leaf curling, yellowing, and stunted growth. No cure exists — prevention is key.",
            "treatment": [
                "Remove and destroy all infected plants immediately.",
                "Control whitefly populations using yellow sticky traps.",
                "Apply insecticides (imidacloprid) to control whiteflies.",
                "Use reflective mulch to repel whiteflies.",
                "Plant TYLCV-resistant tomato varieties."
            ],
            "severity": "Critical",
            "prevention": "Use insect-proof netting. Inspect transplants carefully."
        },
        "hi": {
            "name": "टमाटर का पीला पत्ती मरोड़ वायरस",
            "description": "सफेद मक्खी द्वारा फैलने वाला वायरल रोग।",
            "treatment": [
                "संक्रमित पौधे तुरंत हटाएं।",
                "पीले चिपकने वाले जाल लगाएं।",
                "imidacloprid कीटनाशक का उपयोग करें।"
            ],
            "severity": "गंभीर",
            "prevention": "कीट-रोधी जाल का उपयोग करें।"
        }
    },

    "Tomato__Tomato_mosaic_virus": {
        "en": {
            "name": "Tomato Mosaic Virus",
            "description": "A viral disease causing mosaic patterns (light and dark green patches) on leaves, leaf distortion, and reduced fruit quality.",
            "treatment": [
                "Remove and destroy infected plants immediately — no cure.",
                "Wash hands thoroughly before handling plants.",
                "Control aphid populations that spread the virus.",
                "Disinfect all gardening tools regularly.",
                "Plant virus-resistant tomato varieties."
            ],
            "severity": "High",
            "prevention": "Use certified virus-free seeds. Control insect vectors."
        },
        "hi": {
            "name": "टमाटर का मोजेक वायरस",
            "description": "वायरल रोग जो पत्तियों पर हल्के-गहरे हरे धब्बे बनाता है।",
            "treatment": [
                "संक्रमित पौधे तुरंत हटाएं।",
                "हाथ अच्छी तरह धोएं।",
                "माहू कीट नियंत्रण करें।"
            ],
            "severity": "अधिक",
            "prevention": "प्रमाणित वायरस-मुक्त बीज उपयोग करें।"
        }
    },

    "Tomato_healthy": {
        "en": {
            "name": "Healthy Tomato",
            "description": "Your tomato plant is healthy! No disease detected.",
            "treatment": [
                "Continue current care routine.",
                "Monitor weekly for any signs of disease.",
                "Ensure consistent watering and fertilizing."
            ],
            "severity": "None",
            "prevention": "Rotate crops seasonally. Stake plants for good air circulation."
        },
        "hi": {
            "name": "स्वस्थ टमाटर का पौधा",
            "description": "आपका टमाटर का पौधा स्वस्थ है!",
            "treatment": ["नियमित देखभाल जारी रखें।"],
            "severity": "कोई नहीं",
            "prevention": "फसल चक्र अपनाएं।"
        }
    },
}

# Severity color mapping
SEVERITY_COLORS = {
    "None":     "#4CAF50",
    "Moderate": "#FF9800",
    "High":     "#F44336",
    "Critical": "#B71C1C",
    "कोई नहीं": "#4CAF50",
    "मध्यम":    "#FF9800",
    "अधिक":     "#F44336",
    "गंभीर":    "#B71C1C",
}

def get_disease_info(class_name: str, lang: str = "en") -> dict:
    info = DISEASE_INFO.get(class_name)
    if info is None:
        return {
            "name": class_name.replace("___", " - ").replace("_", " ").title(),
            "description": "No detailed information available for this disease yet.",
            "treatment": ["Consult a local agricultural expert for treatment advice."],
            "severity": "Unknown",
            "prevention": "Monitor the plant regularly and consult an expert."
        }
    lang_info = info.get(lang, info.get("en", {}))
    return lang_info

def get_severity_color(severity: str) -> str:
    return SEVERITY_COLORS.get(severity, "#9E9E9E")
