# Sonar Scanner

## Intallation

In [sonar scanner cli binaries](https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/). You can check current version [here](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/).

## Definition of sonar-project.properties

- **sonar.projectKey:** Name of the project in sonar server. If you leave the same of another existing project when analyzing it will crush the info.
- **sonar.sources:** Folders to analyze
- **sonar.coverage.exclusions:** Folders excluded from scanning for code coverage
- **sonar.exclusions:** Folders excluded for analysis
- **sonar.host.url:** Sonar Platform Host
- **sonar.login:** Access token for the host
- **sonar.python.xunit.reportPath:** Coverage file to mark past lines in xml format
- **sonar.python.coverage.reportPath:** Coverage file to mark past lines

### More infor in [Official Site](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/)
