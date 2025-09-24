# Contributing

Thanks for considering to contribute to Ordeq!
All contributions are welcome, whether it's reporting issues, suggesting features, or submitting code changes.
This should get you started:

- Have a look at the [open issues][open-issues]
- Have a look at our guidelines below
- Set up your local environment as instructed below

## Guidelines

Feel free to challenge the below contributing guidelines.
We are young project and still figuring out how we can collaborate best.

### Development & testing

























Install Ordeq locally in editable mode:





(In case of any issues, check out the troubleshooting section below)

Install the pre-commit hooks:


uv run pre-commit install






- The merge type can be squash commit or merge, provided the commit messages are descriptive enough.

    - the build has succeeded (formatting, linters & tests pass)
    - open comments are resolved
    - at least one person besides the author has approved

### Releases



- Releases should be done for each package individually, e.g. `ordeq`,`ordeq-spark`
- Releases should only be made from the `main` branch. To create a release:

    - Create a git tag on the latest commit: `git tag -a "{package}/{version}" -m "{message}"`. The message can be used to highlight the most significant change in this release.
    - Push the tags to the remote: `git push --tags`
    - The CI pipeline will be triggered by the pushed tag and automatically build the release

### Troubleshooting

#### Locked dependencies

If you get an error saying: `error: Failed to parse 'uv.lock'` or `The lockfile at 'uv.lock' needs to be updated`,
this usually indicates that the dependencies were altered in the `pyproject.toml` or `uv.lock`.

- Please check if you have accidentally altered `pyproject.toml` or `uv.lock`
- Use `uv add` instead of (`uv`) `pip install`. More info [here](https://docs.astral.sh/uv/concepts/projects/dependencies/).

#### Non-pip dependencies

If you receive the following error installing `pymssql` on Mac,
you need to install FreeTDS to get the required C-headers: `brew install freetds`.

```text
  × Failed to build `pymssql==2.3.7`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)
```

#### Docker-backed Tests

Some of the unit tests rely on Docker via the [`testcontainers`][tesco] PyPI package.
If you're using Docker Desktop on macOS, these tests will fail in the default configuration:

```text
ERROR tests/.../test_xxx.py::TestFile::test_function - docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', FileNotFoundError(2, 'No such file or directory'))
```

This can be remedied by changing the configuration of Docker Desktop for macOS:

1. Open Docker Desktop, go to Settings ⇒ Advanced
2. Enable "Docker CLI Tools System ⇒ (requires password)"
3. Enable "Allow default Docker socket (requires password)"
4. Click "Apply & Restart"

[tesco]: https://pypi.org/project/testcontainers/

#### Spark & Java

The unit tests for `ordeq-spark` run Spark on your host system.
This means that Java must be installed on your laptop, and your default Java VM must not be newer than JDK 17, because newer versions remove some deprecated functions that Spark still relies on:

```text
E                   py4j.protocol.Py4JJavaError: An error occurred while calling None.org.apache.spark.api.java.JavaSparkContext.
E                   : java.lang.ExceptionInInitializerError
E                   	at org.apache.spark.unsafe.array.ByteArrayMethods.<clinit>(ByteArrayMethods.java:56)
                        ...
E                   Caused by: java.lang.NoSuchMethodException: java.nio.DirectByteBuffer.<init>(long,int)
                        ...
```

If you use [SdkMan!][sdkm] to manage your Java installations:

```shell
sdk list java | fgrep 17 | fgrep tem
sdk install java 17.0.12-tem   # replace 12 by whatever is current
sdk default java 17.0.12-tem
```

If you use another tool to manage your JDKs, run the equivalent tasks to make sure your `JAVA_HOME` is set correctly.

[sdkm]: https://sdkman.io/

[open-issues]: github.com/ing-bank/ordeq/issues/
