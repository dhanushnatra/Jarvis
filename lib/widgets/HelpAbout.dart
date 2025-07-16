import 'package:flutter/material.dart';
import 'package:jarvis/utils/Colors.dart';

class Helpabout extends StatelessWidget {
  const Helpabout({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.bottomRight,
      decoration: BoxDecoration(color: colors["card"]),
      child: ListView(
        padding: EdgeInsets.only(left: 10, top: 30),
        children: [
          Text(
            "> help",
            style: Theme.of(
              context,
            ).textTheme.headlineSmall?.copyWith(color: colors["primary"]),
          ),
          Text("""
      hold anywhere and speak any following commands

      - remind/schedule me <task>
      - search for <context> on the web
      - open settings
      - what are tasks <on?> <today/tomorrow/date>
      - mail to <mail-id> <context> <formal/informal>
      - turn file sharing <on/off>
      - wake me up in <number> <minutes/hours>
      - open file sharing
      - clear <chat/tasks>
      - jarvis <sleep/wakeup/shutdown>
      - any random question""", style: Theme.of(context).textTheme.bodySmall),
          Text(
            "> about",
            style: Theme.of(
              context,
            ).textTheme.headlineSmall?.copyWith(color: colors["primary"]),
          ),
          Text("""
      jarvis V1

      by    : dhanushnatra
      Tech  : Flutter, fastapi ,docker 
      visit : https://github.com/dhanushnatra/jarvis
      """, style: Theme.of(context).textTheme.bodySmall),
        ],
      ),
    );
  }
}
