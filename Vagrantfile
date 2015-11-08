# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'virtualbox'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.define "ubuntutest" do |ubuntutest|
        ubuntutest.vm.hostname = "ubuntutest"
        ubuntutest.vm.box = "trusty-server"
        ubuntutest.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
    end
    config.vm.provider :virtualbox do |vb|
        vb.memory = 1024
        vb.cpus = 1
    end

    config.vm.provision :shell, path: "bootstrap.sh"
    config.vm.network "public_network"
end
