## Inspiration
The recent AI revolution has been dominated by chatbots and language models, but we saw an opportunity to harness the power of computer vision to create something new. We asked ourselves: what if technology could be controlled with just a glance? Imagine being able to scroll through an article on your laptop while eating lunch, or navigating your tablet with ease, hands-free. We realized that existing solutions for people with disabilities were often outdated, expensive, or required specialized hardware and software. This sparked our idea to apply recent advancements in computer vision to create EyeScreen, an innovative solution that makes technology more accessible and intuitive for everyone.

## What it does
Imagine a world where technology responds to your every glance. With EyeScreen, you can control your computer, navigate your digital life, and interact with the world around you with just a look. Our revolutionary technology harnesses the power of face-tracking to unlock a new era of intuitive, hands-free control.

## Using EyeScreen, you can:

Navigate your computer system with your eyes, moving the cursor with a glance
Click and interact with your computer using subtle facial expressions, such as blinking for left and right clicks
Activate speech-to-text with a simple mouth movement
Browse the internet and manage auto-scroll with precise eye movements and eyebrow gestures
With EyeScreen, you can achieve all the functionality of a traditional keyboard and trackpad, hands-free. Our technology empowers you to interact with your computer in a more natural, intuitive way, using the subtle movements of your face and eyes.
How we built it
We leveraged a combination of cutting-edge technologies to bring EyeScreen to life. Our tech stack includes:

OpenCV2 for real-time face tracking and live-stream camera processing
MediaPipe's Face Landmark technology to accurately track facial muscles and eye movements
NumPy for efficient array and matrix data processing
PyAutoGUI for simulating user interactions, such as cursor movement, clicks, and navigation
Apple's built-in Speech-to-Text dictation technology for seamless voice input
By integrating these technologies, we created a robust and efficient system that enables users to control their devices with ease. Our architecture allows for real-time processing of facial expressions, eye movements, and voice commands, providing a seamless and intuitive user experience.
## Challenges we ran into
A constant challenge during the development of EyeScreen was prioritizing input commands due to the limited number of distinct facial features we could track. With only a finite range of facial expressions and movements available, we needed to determine which commands would be most intuitive and useful while avoiding confusion and overlap.

Balancing a responsive control system with the constraints of facial recognition technology required us to carefully evaluate which facial movements could be reliably detected and effectively used. We explored various methods to make the most of each facial feature, ensuring that the controls remained intuitive and user-friendly.

## Accomplishments that we're proud of
We’re incredibly proud of what we’ve achieved with EyeScreen. Our innovative system seamlessly transforms facial movements into intuitive, hands-free control, breaking new ground in accessibility and user experience. By expertly integrating cutting-edge technologies like OpenCV2, MediaPipe, and PyAutoGUI, we’ve crafted a real-time, high-performance solution that’s both responsive and intuitive. EyeScreen not only sets a new standard for interacting with technology but also opens doors for more inclusive and adaptive computing.

## What we learned
During the development of EyeScreen, we gained crucial insights into mapping and interpreting facial movements, including eye, eyebrow, mouth, and blinking actions. We discovered that accurately tracking these subtle movements required a delicate balance between precision and real-time performance.

Mapping eye and eyebrow movements taught us how to translate these gestures into intuitive controls, such as scrolling and navigation, while ensuring the system remained responsive and reliable. We learned to refine our algorithms to distinguish between various expressions and gestures, enhancing the system’s ability to interpret user intentions accurately.

## What's next for EyeScreen
Development is an ongoing process, but the technology is now fully ready for everyday use. It performs all the tasks a standard keyboard and mouse can handle, and offers additional functionalities that extend beyond basic tools. With intuitive controls and comprehensive features already integrated, the technology is designed to be an affordable solution accessible to anyone with a computer. The next step is to focus on distribution, ensuring that it reaches those who can benefit from it most.


