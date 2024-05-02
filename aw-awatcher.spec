# * no tests available
%bcond_with check

%global commit0 be59315e8a7c7be3bbeafc60b68a06d1507b2a2a
%global short_commit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/aw-server-rust
%global commit1 448312d410980d4a92a0fb4d4bb3fa3494cf6c89
%global short_commit1 %(c=%{commit1}; echo ${c:0:7})

Name:           aw-awatcher
Version:        0.2.5^20240507.%{short_commit0}
Release:        %autorelease
Summary:        A window activity and idle watcher

License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0 AND (Apache-2.0 OR ISC OR MIT AND (Apache-2.0 OR MIT AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND ISC AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://github.com/2e3s/awatcher
Source0:        %{url}/archive/%{commit0}/awatcher-%{short_commit0}.tar.gz
Source1:        %{url1}/archive/%{commit1}/aw-server-rust-%{short_commit1}.tar.gz

Requires:       aw-server-rust
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  help2man

%description
%{summary}

# (Apache-2.0 OR MIT) AND BSD-3-Clause: encoding_rs v0.8.34
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.8.3
# : aw-client-rust v0.1.0
# : aw-models v0.1.0
# : awatcher v0.2.6
# : watchers v0.2.6
# Apache-2.0 OR BSL-1.0: ryu v1.0.18
# Apache-2.0 OR ISC OR MIT: rustls-pemfile v1.0.4
# Apache-2.0 OR MIT: async-channel v2.2.1
# Apache-2.0 OR MIT: async-executor v1.11.0
# Apache-2.0 OR MIT: async-fs v1.6.0
# Apache-2.0 OR MIT: async-io v1.13.0
# Apache-2.0 OR MIT: async-lock v2.8.0
# Apache-2.0 OR MIT: async-lock v3.3.0
# Apache-2.0 OR MIT: async-task v4.7.0
# Apache-2.0 OR MIT: atomic-waker v1.1.2
# Apache-2.0 OR MIT: blocking v1.5.1
# Apache-2.0 OR MIT: concurrent-queue v2.4.0
# Apache-2.0 OR MIT: equivalent v1.0.1
# Apache-2.0 OR MIT: event-listener v2.5.3
# Apache-2.0 OR MIT: event-listener v4.0.3
# Apache-2.0 OR MIT: event-listener v5.3.0
# Apache-2.0 OR MIT: event-listener-strategy v0.4.0
# Apache-2.0 OR MIT: event-listener-strategy v0.5.0
# Apache-2.0 OR MIT: fastrand v1.9.0
# Apache-2.0 OR MIT: fastrand v2.0.2
# Apache-2.0 OR MIT: fnv v1.0.7
# Apache-2.0 OR MIT: futures-lite v1.13.0
# Apache-2.0 OR MIT: futures-lite v2.3.0
# Apache-2.0 OR MIT: indexmap v2.2.6
# Apache-2.0 OR MIT: parking v2.2.0
# Apache-2.0 OR MIT: pin-project-lite v0.2.14
# Apache-2.0 OR MIT: polling v2.8.0
# Apache-2.0 OR MIT: signal-hook-registry v1.4.2
# Apache-2.0 OR MIT: utf8parse v0.2.1
# Apache-2.0 OR MIT: waker-fn v1.1.1
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: io-lifetimes v1.0.11
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.3.8
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.4.12
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v0.37.26
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v0.38.34
# Apache-2.0: gethostname v0.4.3
# Apache-2.0: openssl v0.10.64
# Apache-2.0: sync_wrapper v1.0.1
# ISC: libloading v0.8.3
# MIT OR Apache-2.0 OR Zlib: tinyvec_macros v0.1.1
# MIT OR Apache-2.0: anstream v0.6.13
# MIT OR Apache-2.0: anstyle v1.0.7
# MIT OR Apache-2.0: anstyle-parse v0.2.4
# MIT OR Apache-2.0: anstyle-query v1.0.3
# MIT OR Apache-2.0: anyhow v1.0.82
# MIT OR Apache-2.0: async-broadcast v0.5.1
# MIT OR Apache-2.0: base64 v0.21.7
# MIT OR Apache-2.0: bitflags v1.3.2
# MIT OR Apache-2.0: bitflags v2.5.0
# MIT OR Apache-2.0: block-buffer v0.10.4
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: chrono v0.4.38
# MIT OR Apache-2.0: clap v4.5.4
# MIT OR Apache-2.0: clap_builder v4.5.2
# MIT OR Apache-2.0: clap_lex v0.7.0
# MIT OR Apache-2.0: colorchoice v1.0.1
# MIT OR Apache-2.0: cpufeatures v0.2.12
# MIT OR Apache-2.0: crossbeam-utils v0.8.19
# MIT OR Apache-2.0: crypto-common v0.1.6
# MIT OR Apache-2.0: digest v0.10.7
# MIT OR Apache-2.0: dirs v5.0.1
# MIT OR Apache-2.0: dirs-sys v0.4.1
# MIT OR Apache-2.0: downcast-rs v1.2.1
# MIT OR Apache-2.0: dyn-clone v1.0.17
# MIT OR Apache-2.0: enumflags2 v0.7.9
# MIT OR Apache-2.0: errno v0.3.8
# MIT OR Apache-2.0: foreign-types v0.3.2
# MIT OR Apache-2.0: foreign-types-shared v0.1.1
# MIT OR Apache-2.0: form_urlencoded v1.2.1
# MIT OR Apache-2.0: futures-channel v0.3.30
# MIT OR Apache-2.0: futures-core v0.3.30
# MIT OR Apache-2.0: futures-io v0.3.30
# MIT OR Apache-2.0: futures-sink v0.3.30
# MIT OR Apache-2.0: futures-task v0.3.30
# MIT OR Apache-2.0: futures-util v0.3.30
# MIT OR Apache-2.0: getrandom v0.2.14
# MIT OR Apache-2.0: hashbrown v0.14.3
# MIT OR Apache-2.0: hex v0.4.3
# MIT OR Apache-2.0: http v0.2.12
# MIT OR Apache-2.0: httparse v1.8.0
# MIT OR Apache-2.0: httpdate v1.0.3
# MIT OR Apache-2.0: hyper-tls v0.5.0
# MIT OR Apache-2.0: iana-time-zone v0.1.60
# MIT OR Apache-2.0: idna v0.5.0
# MIT OR Apache-2.0: ipnet v2.9.0
# MIT OR Apache-2.0: itoa v1.0.11
# MIT OR Apache-2.0: lazy_static v1.4.0
# MIT OR Apache-2.0: libc v0.2.154
# MIT OR Apache-2.0: log v0.4.21
# MIT OR Apache-2.0: mime v0.3.17
# MIT OR Apache-2.0: native-tls v0.2.11
# MIT OR Apache-2.0: num-traits v0.2.19
# MIT OR Apache-2.0: once_cell v1.19.0
# MIT OR Apache-2.0: openssl-probe v0.1.5
# MIT OR Apache-2.0: ordered-stream v0.2.0
# MIT OR Apache-2.0: percent-encoding v2.3.1
# MIT OR Apache-2.0: pin-utils v0.1.0
# MIT OR Apache-2.0: piper v0.2.1
# MIT OR Apache-2.0: ppv-lite86 v0.2.17
# MIT OR Apache-2.0: rand v0.8.5
# MIT OR Apache-2.0: rand_chacha v0.3.1
# MIT OR Apache-2.0: rand_core v0.6.4
# MIT OR Apache-2.0: regex v1.10.4
# MIT OR Apache-2.0: regex-automata v0.4.6
# MIT OR Apache-2.0: reqwest v0.11.27
# MIT OR Apache-2.0: scoped-tls v1.0.1
# MIT OR Apache-2.0: serde v1.0.200
# MIT OR Apache-2.0: serde_json v1.0.116
# MIT OR Apache-2.0: serde_spanned v0.6.5
# MIT OR Apache-2.0: serde_urlencoded v0.7.1
# MIT OR Apache-2.0: sha1 v0.10.6
# MIT OR Apache-2.0: smallvec v1.13.2
# MIT OR Apache-2.0: socket2 v0.4.10
# MIT OR Apache-2.0: socket2 v0.5.6
# MIT OR Apache-2.0: static_assertions v1.1.0
# MIT OR Apache-2.0: toml v0.8.12
# MIT OR Apache-2.0: toml_datetime v0.6.5
# MIT OR Apache-2.0: toml_edit v0.22.12
# MIT OR Apache-2.0: typenum v1.17.0
# MIT OR Apache-2.0: unicode-bidi v0.3.15
# MIT OR Apache-2.0: unicode-normalization v0.1.23
# MIT OR Apache-2.0: url v2.5.0
# MIT OR Apache-2.0: x11rb v0.13.0
# MIT OR Apache-2.0: x11rb-protocol v0.13.0
# MIT: atty v0.2.14
# MIT: bytes v1.6.0
# MIT: dlib v0.5.2
# MIT: fern v0.6.2
# MIT: generic-array v0.14.7
# MIT: h2 v0.3.26
# MIT: http-body v0.4.6
# MIT: hyper v0.14.28
# MIT: memoffset v0.7.1
# MIT: mio v0.8.11
# MIT: nix v0.26.4
# MIT: openssl-sys v0.9.102
# MIT: schemars v0.8.19
# MIT: slab v0.4.9
# MIT: strsim v0.11.1
# MIT: tokio v1.37.0
# MIT: tokio-native-tls v0.3.1
# MIT: tokio-util v0.7.10
# MIT: tower-service v0.3.2
# MIT: tracing v0.1.40
# MIT: tracing-core v0.1.32
# MIT: try-lock v0.2.5
# MIT: want v0.3.1
# MIT: wayland-backend v0.3.3
# MIT: wayland-client v0.31.2
# MIT: wayland-protocols v0.31.2
# MIT: wayland-protocols-plasma v0.2.0
# MIT: wayland-protocols-wlr v0.2.0
# MIT: wayland-sys v0.31.1
# MIT: winnow v0.6.6
# MIT: xdg-home v1.1.0
# MIT: zbus v3.15.2
# MIT: zbus_names v2.6.1
# MIT: zvariant v3.15.2
# MPL-2.0: colored v1.9.3
# MPL-2.0: option-ext v0.2.0
# Unlicense OR MIT: aho-corasick v1.1.3
# Unlicense OR MIT: byteorder v1.5.0
# Unlicense OR MIT: memchr v2.7.2
# Zlib OR Apache-2.0 OR MIT: tinyvec v1.6.0

%prep
%autosetup -n awatcher-%{commit0}
tar -xf %{SOURCE1} --strip-components 1 aw-server-rust-%{commit1}/{aw-client-rust,aw-models}

# don't download anything from the internet
sed -ri 's|git = "https://github.com/ActivityWatch/aw-server-rust", rev = "448312d"|path = "../aw-client-rust"|' watchers/Cargo.toml

# works with 0.24.7 too
sed -ri 's/image = \{ version = "0.25.1" \}/image = \{ version = "0.24.7" \}/' Cargo.toml

# aw-client-rust is just a dependency, so it doesn't need its dev dependencies
sed -ri '/dev-dependencies/,+4d' aw-client-rust/Cargo.toml
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%cargo_license
%cargo_license_summary

%install
%cargo_install
# prefix with aw- in order to be detected a watcher in aw-qt
mv %{buildroot}%{_bindir}/{awatcher,%{name}}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -o %{buildroot}%{_mandir}/man1/%{name}.1

%if %{with check}
%check
%cargo_test
%endif

%files
%doc README.md
%license LICENSE
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
%autochangelog
