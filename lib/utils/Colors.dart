import 'package:flutter/material.dart';

final Map<String, Color> colors = {
  "primary": Color(0xFF00c8ff),
  "secondary": Color(0xFF00ffae),
  "card": Color(0xFF2d2d2d),
};

final theme = ThemeData(
  scaffoldBackgroundColor: Color(0x00242424),
  textTheme: TextTheme(
    bodySmall: TextStyle(
      fontFamily: "ShareTechMono",
      fontSize: 12,
      color: Color.fromARGB(255, 255, 255, 255),
    ),
    headlineLarge: TextStyle(fontFamily: "ShareTechMono", fontSize: 64),
    headlineSmall: TextStyle(fontFamily: "ShareTechMono", fontSize: 20),
  ),
);
