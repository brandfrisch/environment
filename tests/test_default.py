from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_tzdata_installed(Package):
    tzdata = Package('tzdata')

    assert tzdata.is_installed


def test_locales_installed(Package):
    locales = Package('locales')

    assert locales.is_installed


def test_correctly_linked_localtime(File):
    localtime = File('/etc/localtime')

    assert localtime.is_symlink


def test_etc_timezone(File):
    timezone = File('/etc/timezone')

    assert timezone.content == 'Etc/UTC\n'
