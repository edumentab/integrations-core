# CHANGELOG - ProxySQL

## 3.4.0 / 2022-02-19

* [Added] Add `pyproject.toml` file. See [#11422](https://github.com/DataDog/integrations-core/pull/11422).
* [Fixed] Fix namespace packaging on Python 2. See [#11532](https://github.com/DataDog/integrations-core/pull/11532).

## 3.3.1 / 2022-01-08 / Agent 7.34.0

* [Fixed] Add comment to autogenerated model files. See [#10945](https://github.com/DataDog/integrations-core/pull/10945).

## 3.3.0 / 2021-11-02 / Agent 7.33.0

* [Added] Add pool.latency_us and correct unit for pool.latency_ms. See [#10335](https://github.com/DataDog/integrations-core/pull/10335).

## 3.2.0 / 2021-10-04 / Agent 7.32.0

* [Added] Disable generic tags. See [#10027](https://github.com/DataDog/integrations-core/pull/10027).

## 3.1.0 / 2021-08-22 / Agent 7.31.0

* [Added] Add runtime configuration validation. See [#8975](https://github.com/DataDog/integrations-core/pull/8975).
* [Added] Support `SHUNNED_REPLICATION_LAG` status for `proxysql.backend.status` service check. See [#9738](https://github.com/DataDog/integrations-core/pull/9738).

## 3.0.1 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 3.0.0 / 2021-01-25 / Agent 7.26.0

* [Added] Add version verification for datadog-checks-base. See [#8255](https://github.com/DataDog/integrations-core/pull/8255).
* [Changed] Update ProxySQL check to use TLS context wrapper. See [#8243](https://github.com/DataDog/integrations-core/pull/8243).

## 2.0.0 / 2020-10-31 / Agent 7.24.0

* [Fixed] Fix config typo. See [#7843](https://github.com/DataDog/integrations-core/pull/7843).
* [Changed] QueryManager - Prevent queries leaking between check instances. See [#7750](https://github.com/DataDog/integrations-core/pull/7750).

## 1.2.2 / 2020-09-21 / Agent 7.23.0

* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 1.2.1 / 2020-07-03 / Agent 7.21.0

* [Fixed] Revert/Remove unnecessary `database_name` config. See [#7049](https://github.com/DataDog/integrations-core/pull/7049).

## 1.2.0 / 2020-06-29

* [Added] Allow proxysql checks to specify stats database name. See [#6835](https://github.com/DataDog/integrations-core/pull/6835). Thanks [tabacco](https://github.com/tabacco).

## 1.1.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.0.0 / 2020-04-03 / Agent 7.19.0

* [Added] New Integration ProxySQL. See [#6144](https://github.com/DataDog/integrations-core/pull/6144).
