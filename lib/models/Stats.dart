class ServerStats {
  final double cpu;
  final double temp;
  final double ram;

  ServerStats({required this.cpu, required this.temp, required this.ram});

  factory ServerStats.fromJson(Map<String, double> json) {
    return ServerStats(
      cpu: json['cpu'] ?? 0,
      temp: json['temp'] ?? 0,
      ram: json['ram'] ?? 0,
    );
  }
}
