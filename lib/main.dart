import 'package:flutter/material.dart';
import 'package:jarvis/widgets/HelpAbout.dart';
import 'package:jarvis/utils/Colors.dart';

void main() {
  return runApp(const Jarvis());
}

class Jarvis extends StatelessWidget {
  const Jarvis({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: theme,
      home: Scaffold(
        body: SizedBox(
          width: MediaQuery.of(context).size.width,
          height: MediaQuery.of(context).size.height,
          child: Helpabout(),
        ),
      ),
    );
  }
}
