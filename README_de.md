# Fix DB WiFi

### [English Readme](README.md)

____

`fix-db-wifi` ist ein einfaches CLI tool zur Behebung von Verbindungsproblemen zwischen Ubuntu Geräten und dem ICE WiFi.
Das Problem wird ausgelöst durch IP-Adresskonflikte zwischen dem WiFi der Deutschen Bahn und
Docker-Netzwerken. Sowohl das WiFi der Deutschen Bahn als auch Docker verwenden standardmäßig den Adressraum
`172.18.0.0/16`, was zu Verbindungsproblemen führt. Dieses Tool entfernt entweder alle Docker-Netzwerke in diesem
Adressraum, oder passt den standardmäßigen Adresspool von Docker dauerhaft an, um den Konflikt zu
vermeiden.

## Funktionsweise

Dieses Tool hat zwei Funktionen:

### `--temporary` (default)

Entfernt alle Docker-Netzwerke im besagten Adressraum. Betroffene Docker container müssen neu gestartet werden.

### `--permanent`

Mit dem `--permanent` flag modifiziert das Tool die Konfigurationsdatei von Docker (`/etc/docker/daemon.json`), um den
standardmäßigen Adresspool auf `192.168.0.0/16` zu ändern und startet Docker dann neu.

## Benutzung

Um `fix-db-wifi` zu installieren, verwenden Sie pip in Ihrem Terminal:

```bash
pip install fix_db_wifi
```

Danach können Sie das Tool mit

```bash
fix_db_wifi
```

oder

```bash
fix_db_wifi --permanent
```

ausführen.

Zu beachten:

- `fix-db-wifi` aufgrund der durchgeführten Änderungen an IP Einstellungen mit Root-Rechten ausgeführt werden muss.
- Andere Verbindungsprobleme als der Konflikt mit Docker werden nicht behandelt.
- Die ursprüngliche Lösung stammt von [hier](https://forum.ubuntuusers.de/topic/probleme-mit-dem-wifionice/).
- Bei Problemen gerne ein Issue eröffnen


