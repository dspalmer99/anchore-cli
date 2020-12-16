import pytest
from anchorecli.cli import system
from click.testing import CliRunner


class TestSystemSubcommandHelp:
    @pytest.mark.parametrize(
        "subcommand, output_start",
        [
            (system.status, "Usage: status"),
            (system.describe_errorcodes, "Usage: errorcodes"),
            (system.wait, "Usage: wait"),
            (system.delete, "Usage: del"),
            (system.feeds, "Usage: feeds"),
            (system.list, "Usage: list"),
            (system.feedsync, "Usage: sync"),
            (system.toggle_enabled, "Usage: config"),
            (system.delete_data, "Usage: delete"),
        ],
    )
    def test_event_subcommand_help(self, subcommand, output_start):
        runner = CliRunner()
        result = runner.invoke(subcommand, ["--help"])
        assert result.exit_code == 0
        assert result.output.startswith(output_start)
