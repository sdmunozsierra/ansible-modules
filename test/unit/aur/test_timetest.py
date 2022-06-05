import mock

from aur import timetest


class TestFirstMod:

    @mock.patch("aur.timetest.AnsibleModule", autospec=True)
    def test__main__success(self, ansible_mod_cls):
        firstmod.main()

        expected_arguments_spec = dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/timetest")
        )
        assert(mock.call(argument_spec=expected_arguments_spec) ==
               ansible_mod_cls.call_args)
