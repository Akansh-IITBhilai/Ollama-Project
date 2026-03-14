# 🤖 AI Assistant with Customizable UI

A beautiful, modern AI chat interface built with Streamlit and powered by Ollama's local language models.

## 📋 Project Overview

This project features a modern Streamlit application that provides an interactive chat interface with local AI models, featuring customizable backgrounds and enhanced user experience.

## 🚀 Features

### ✨ Enhanced UI (ui.py)
- **🎨 Custom Backgrounds**: Change background images with URL input or preset options
- **💬 Chat Interface**: Clean conversation history with user/bot message bubbles
- **⚙️ Model Selection**: Choose between different AI models (tinyllama, phi, gemma:2b)
- **🎯 Enhanced Visibility**: Advanced text contrast techniques for readability on any background
- **📱 Responsive Design**: Modern glassmorphism effects and smooth animations
- **🔄 Persistent Settings**: Background and chat history maintained during session

### 🔧 Technical Features
- **Local AI**: Runs entirely on your machine using Ollama
- **Memory Efficient**: Uses smaller models that fit in limited RAM
- **Fast Responses**: Direct integration with Ollama API
- **Error Handling**: Graceful error messages and loading states

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Ollama installed and running
- At least 3GB RAM available

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Ollama Models
```bash
# Install the smaller models for better compatibility
ollama pull tinyllama
ollama pull phi
ollama pull gemma:2b
```

### 3. Run the Application
```bash
# Run the enhanced AI assistant
streamlit run ui.py
```

## 🎨 Customization

### Background Images
- **Custom URLs**: Enter any image URL in the sidebar
- **Preset Backgrounds**: Quick one-click options:
  - 🌊 Ocean scenes
  - 🌌 Space themes
  - 🌲 Forest landscapes
  - 🏙️ City skylines

### AI Models
Choose from available models based on your system's capabilities:
- **tinyllama**: Fastest, lowest memory usage (~1.1B parameters)
- **phi**: Balanced performance (~2.7B parameters)
- **gemma:2b**: Google's efficient model (~2B parameters)

## 📁 Project Structure
```
Ollama_project/
├── ui.py                # Enhanced modern AI assistant interface
├── requirements.txt     # Python dependencies
└── SUMMARY.md          # Project documentation
```

## 🔧 Dependencies
- **streamlit**: Web app framework
- **ollama**: Local AI model integration

## 🚨 Troubleshooting

### Memory Issues
If you get "model requires more system memory" errors:
1. Use `tinyllama` model (smallest memory footprint)
2. Close other memory-intensive applications
3. Consider upgrading system RAM

### Network Issues
If model downloads fail:
1. Check internet connection
2. Try different models
3. Use VPN if needed

### Text Visibility
For background image visibility issues:
- Use darker backgrounds for better contrast
- The enhanced UI has automatic text highlighting
- Try preset backgrounds for optimal readability

## 👨‍💻 Development

### Adding New Features
- Modify `ui.py` for UI enhancements and new functionality
- Add new models to the `available_models` list
- Extend background presets in the sidebar

### Custom Styling
- Edit the CSS section in `ui.py`
- Use CSS variables for consistent theming
- Test on different background types

## 📄 License

This project is created for educational and personal use.

## 🙏 Credits

**Created by:** Akansh Tyagi
**Dedicated to:** My family - Hamendra, Shalini, and Aditya Tyagi

**Technologies Used:**
- Streamlit for the web interface
- Ollama for local AI model hosting
- Custom CSS for modern UI design

---

*Enjoy your personalized AI assistant! 🌟*</content>
<parameter name="filePath">c:\Users\akans\OneDrive\Desktop\Folders\Projects\Ollama_project\README.md