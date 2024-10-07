#!/usr/bin/make -f

VERSION:=0.1.7
DEBVERSION:=1
ifndef DIST
	DIST=jammy
endif

clean:
	rm -f *.dsc *.debian.tar.xz *.buildinfo *.changes *.deb *.upload
	rm -Rf libvirt-guests-delayed-$(VERSION)

libvirt-guests-delayed-$(VERSION):
	mkdir libvirt-guests-delayed-$(VERSION)
	cp -a guests_delayed.* libvirt-guests-delayed-$(VERSION)/

libvirt-guests-delayed_$(VERSION).orig.tar.gz: libvirt-guests-delayed-$(VERSION)
	tar cvzf libvirt-guests-delayed_$(VERSION).orig.tar.gz libvirt-guests-delayed-$(VERSION)/

libvirt-guests-delayed-$(VERSION)/debian: libvirt-guests-delayed-$(VERSION)
	cp -Rf debian libvirt-guests-delayed-$(VERSION)/
	cp -a README.md libvirt-guests-delayed-$(VERSION)/debian/
	cp -a libvirt-guests-delayed.service libvirt-guests-delayed-$(VERSION)/debian/

libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)_source.changes: clean libvirt-guests-delayed-$(VERSION)/debian
	cd libvirt-guests-delayed-$(VERSION) && dch -l "~${DIST}" --distribution "${DIST}" "Build for PPA"
	cd libvirt-guests-delayed-$(VERSION) && dpkg-buildpackage -S
	lintian libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)~${DIST}1_source.changes
	dput myppa:libvirt-guests-delayed libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)~${DIST}1_source.changes

ppa: libvirt-guests-delayed_$(VERSION).orig.tar.gz
	$(MAKE) DIST=noble libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)_source.changes
	$(MAKE) DIST=jammy libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)_source.changes
	$(MAKE) DIST=focal libvirt-guests-delayed_$(VERSION)-$(DEBVERSION)_source.changes
