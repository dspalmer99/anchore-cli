import pytest
from anchorecli.cli import event
from click.testing import CliRunner


class TestEventSubcommandHelp:
    @pytest.mark.parametrize(
        "subcommand, output_start",
        [
            (event.list, "Usage: list"),
            (event.get, "Usage: get"),
            (event.delete, "Usage: delete"),
        ]
    )
    def test_event_subcommand_help(self, subcommand, output_start):
        runner = CliRunner()
        result = runner.invoke(subcommand, ["--help"])
        assert result.exit_code == 0
        assert result.output.startswith(output_start)
