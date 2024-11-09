%bcond_with check

%global commit a0cdef90cf86cd8d2cc89723f5751c1123ae7e2b
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           aw-server-rust
Version:        0.13.1^20241109.%{short_commit}
Release:        %autorelease
Summary:        A re-implementation of aw-server in Rust

#(Apache-2.0 OR MIT) AND BSD-3-Clause: encoding_rs v0.8.34
#(MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.8.5
#0BSD OR MIT OR Apache-2.0: adler2 v2.0.0
#: aw-client-rust v0.1.0
#: aw-datastore v0.1.0
#: aw-models v0.1.0
#: aw-query v0.1.0
#: aw-server v0.13.1+a0cdef9
#: aw-sync v0.1.0
#: aw-transform v0.1.0
#Apache-2.0 OR BSL-1.0: ryu v1.0.18
#Apache-2.0 OR ISC OR MIT: rustls-pemfile v1.0.4
#Apache-2.0 OR MIT: addr2line v0.24.2
#Apache-2.0 OR MIT: atomic v0.5.3
#Apache-2.0 OR MIT: atomic v0.6.0
#Apache-2.0 OR MIT: equivalent v1.0.1
#Apache-2.0 OR MIT: fastrand v2.1.1
#Apache-2.0 OR MIT: fnv v1.0.7
#Apache-2.0 OR MIT: indexmap v2.6.0
#Apache-2.0 OR MIT: inlinable_string v0.1.15
#Apache-2.0 OR MIT: object v0.36.5
#Apache-2.0 OR MIT: pin-project-lite v0.2.14
#Apache-2.0 OR MIT: signal-hook-registry v1.4.2
#Apache-2.0 OR MIT: utf8parse v0.2.2
#Apache-2.0 OR MIT: uuid v1.11.0
#Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: linux-raw-sys v0.4.14
#Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT: rustix v0.38.38
#Apache-2.0: gethostname v0.4.3
#Apache-2.0: openssl v0.10.68
#Apache-2.0: sync_wrapper v1.0.1
#BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.7.35
#MIT OR Apache-2.0 OR Zlib: tinyvec_macros v0.1.1
#MIT OR Apache-2.0: ahash v0.8.11
#MIT OR Apache-2.0: anstream v0.6.17
#MIT OR Apache-2.0: anstyle v1.0.9
#MIT OR Apache-2.0: anstyle-parse v0.2.6
#MIT OR Apache-2.0: anstyle-query v1.1.2
#MIT OR Apache-2.0: appdirs v0.2.0
#MIT OR Apache-2.0: backtrace v0.3.74
#MIT OR Apache-2.0: base64 v0.21.7
#MIT OR Apache-2.0: bit-set v0.5.3
#MIT OR Apache-2.0: bit-vec v0.6.3
#MIT OR Apache-2.0: bitflags v2.6.0
#MIT OR Apache-2.0: block-buffer v0.10.4
#MIT OR Apache-2.0: cfg-if v1.0.0
#MIT OR Apache-2.0: chrono v0.4.38
#MIT OR Apache-2.0: clap v4.5.20
#MIT OR Apache-2.0: clap_builder v4.5.20
#MIT OR Apache-2.0: clap_lex v0.7.2
#MIT OR Apache-2.0: colorchoice v1.0.3
#MIT OR Apache-2.0: cookie v0.18.1
#MIT OR Apache-2.0: cpufeatures v0.2.14
#MIT OR Apache-2.0: crossbeam-channel v0.5.13
#MIT OR Apache-2.0: crossbeam-utils v0.8.20
#MIT OR Apache-2.0: crypto-common v0.1.6
#MIT OR Apache-2.0: deranged v0.3.11
#MIT OR Apache-2.0: digest v0.10.7
#MIT OR Apache-2.0: dirs v5.0.1
#MIT OR Apache-2.0: dirs-sys v0.4.1
#MIT OR Apache-2.0: dyn-clone v1.0.17
#MIT OR Apache-2.0: either v1.13.0
#MIT OR Apache-2.0: errno v0.3.9
#MIT OR Apache-2.0: fallible-iterator v0.3.0
#MIT OR Apache-2.0: fallible-streaming-iterator v0.1.9
#MIT OR Apache-2.0: figment v0.10.19
#MIT OR Apache-2.0: foreign-types v0.3.2
#MIT OR Apache-2.0: foreign-types-shared v0.1.1
#MIT OR Apache-2.0: form_urlencoded v1.2.1
#MIT OR Apache-2.0: futures v0.3.31
#MIT OR Apache-2.0: futures-channel v0.3.31
#MIT OR Apache-2.0: futures-core v0.3.31
#MIT OR Apache-2.0: futures-io v0.3.31
#MIT OR Apache-2.0: futures-sink v0.3.31
#MIT OR Apache-2.0: futures-task v0.3.31
#MIT OR Apache-2.0: futures-util v0.3.31
#MIT OR Apache-2.0: getrandom v0.2.15
#MIT OR Apache-2.0: gimli v0.31.1
#MIT OR Apache-2.0: hashbrown v0.14.5
#MIT OR Apache-2.0: hashbrown v0.15.0
#MIT OR Apache-2.0: hashlink v0.9.1
#MIT OR Apache-2.0: http v0.2.12
#MIT OR Apache-2.0: http v1.1.0
#MIT OR Apache-2.0: httparse v1.9.5
#MIT OR Apache-2.0: httpdate v1.0.3
#MIT OR Apache-2.0: hyper-tls v0.5.0
#MIT OR Apache-2.0: iana-time-zone v0.1.61
#MIT OR Apache-2.0: idna v0.5.0
#MIT OR Apache-2.0: ipnet v2.10.1
#MIT OR Apache-2.0: itoa v1.0.11
#MIT OR Apache-2.0: lazy_static v1.5.0
#MIT OR Apache-2.0: libc v0.2.161
#MIT OR Apache-2.0: lock_api v0.4.12
#MIT OR Apache-2.0: log v0.4.22
#MIT OR Apache-2.0: log-panics v2.1.0
#MIT OR Apache-2.0: mime v0.3.17
#MIT OR Apache-2.0: native-tls v0.2.12
#MIT OR Apache-2.0: num-conv v0.1.0
#MIT OR Apache-2.0: num-traits v0.2.19
#MIT OR Apache-2.0: num_cpus v1.16.0
#MIT OR Apache-2.0: once_cell v1.20.2
#MIT OR Apache-2.0: openssl-probe v0.1.5
#MIT OR Apache-2.0: parking_lot v0.12.3
#MIT OR Apache-2.0: parking_lot_core v0.9.10
#MIT OR Apache-2.0: pear v0.2.9
#MIT OR Apache-2.0: percent-encoding v2.3.1
#MIT OR Apache-2.0: pin-utils v0.1.0
#MIT OR Apache-2.0: powerfmt v0.2.0
#MIT OR Apache-2.0: ppv-lite86 v0.2.20
#MIT OR Apache-2.0: rand v0.8.5
#MIT OR Apache-2.0: rand_chacha v0.3.1
#MIT OR Apache-2.0: rand_core v0.6.4
#MIT OR Apache-2.0: ref-cast v1.0.23
#MIT OR Apache-2.0: regex v1.11.1
#MIT OR Apache-2.0: regex-automata v0.4.8
#MIT OR Apache-2.0: reqwest v0.11.27
#MIT OR Apache-2.0: rocket v0.5.1
#MIT OR Apache-2.0: rocket_cors v0.6.0
#MIT OR Apache-2.0: rocket_http v0.5.1
#MIT OR Apache-2.0: rustc-demangle v0.1.24
#MIT OR Apache-2.0: scopeguard v1.2.0
#MIT OR Apache-2.0: sd-notify v0.4.3
#MIT OR Apache-2.0: serde v1.0.210
#MIT OR Apache-2.0: serde_json v1.0.131
#MIT OR Apache-2.0: serde_spanned v0.6.8
#MIT OR Apache-2.0: serde_urlencoded v0.7.1
#MIT OR Apache-2.0: sha2 v0.10.8
#MIT OR Apache-2.0: smallvec v1.13.2
#MIT OR Apache-2.0: socket2 v0.5.7
#MIT OR Apache-2.0: stable-pattern v0.1.0
#MIT OR Apache-2.0: state v0.6.0
#MIT OR Apache-2.0: tempfile v3.13.0
#MIT OR Apache-2.0: time v0.3.36
#MIT OR Apache-2.0: time-core v0.1.2
#MIT OR Apache-2.0: toml v0.8.19
#MIT OR Apache-2.0: toml_datetime v0.6.8
#MIT OR Apache-2.0: toml_edit v0.22.22
#MIT OR Apache-2.0: typenum v1.17.0
#MIT OR Apache-2.0: ubyte v0.10.4
#MIT OR Apache-2.0: uncased v0.9.10
#MIT OR Apache-2.0: unicase v2.8.0
#MIT OR Apache-2.0: unicase_serde v0.1.0
#MIT OR Apache-2.0: unicode-bidi v0.3.17
#MIT OR Apache-2.0: unicode-normalization v0.1.24
#MIT OR Apache-2.0: url v2.5.2
#MIT OR Apache-2.0: yansi v1.0.1
#MIT OR Zlib OR Apache-2.0: miniz_oxide v0.8.0
#MIT: async-stream v0.3.6
#MIT: binascii v0.1.4
#MIT: bytes v1.8.0
#MIT: fancy-regex v0.13.0
#MIT: fern v0.6.2
#MIT: generic-array v0.14.7
#MIT: h2 v0.3.26
#MIT: http-body v0.4.6
#MIT: hyper v0.14.31
#MIT: is-terminal v0.4.13
#MIT: libsqlite3-sys v0.28.0
#MIT: mio v1.0.2
#MIT: multer v3.1.0
#MIT: openssl-sys v0.9.104
#MIT: rusqlite v0.31.0
#MIT: rust-embed v8.5.0
#MIT: rust-embed-utils v8.5.0
#MIT: schemars v0.8.21
#MIT: slab v0.4.9
#MIT: spin v0.9.8
#MIT: strsim v0.11.1
#MIT: tokio v1.41.0
#MIT: tokio-native-tls v0.3.1
#MIT: tokio-stream v0.1.16
#MIT: tokio-util v0.7.12
#MIT: tower-service v0.3.3
#MIT: tracing v0.1.40
#MIT: tracing-core v0.1.32
#MIT: try-lock v0.2.5
#MIT: want v0.3.1
#MIT: winnow v0.6.20
#MPL-2.0: colored v1.9.4
#MPL-2.0: mpsc_requests v0.3.4
#MPL-2.0: option-ext v0.2.0
#Unlicense OR MIT: aho-corasick v1.1.3
#Unlicense OR MIT: byteorder v1.5.0
#Unlicense OR MIT: memchr v2.7.4
#Unlicense OR MIT: same-file v1.0.6
#Unlicense OR MIT: walkdir v2.5.0
#Zlib OR Apache-2.0 OR MIT: bytemuck v1.19.0
#Zlib OR Apache-2.0 OR MIT: tinyvec v1.8.0
License:        ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)

URL:            https://github.com/ActivityWatch/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man
BuildRequires:  nodejs-aw-webui

%description
%{summary}

%prep
%autosetup -n %{name}-%{commit} -p1
# drop an unused, benchmark-only criterion dev-dependency to speed up builds
find -name "*.toml" | xargs sed -ri '/^[[:blank:]]*criterion\b/d'

# switch to SQLite available in Fedora
sed -ri 's/rusqlite = \{ version = "0.30", features = \["chrono", "serde_json", "bundled"\]  \}/rusqlite = \{ version = "0.31", features = \["chrono", "serde_json"\]  \}/' aw-datastore/Cargo.toml

# switch to fancy-regex available in Fedora
sed -ri 's/fancy-regex = "0.12.0"/fancy-regex = "0.13.0"/' aw-query/Cargo.toml aw-transform/Cargo.toml

# append current commit to the version string
sed -ri 's/version = "0.13.1"/version = "0.13.1+%{short_commit}"/' aw-server/Cargo.toml

# remove Android dependencies
sed -ri '/target_os="android"/,+4d' aw-server/Cargo.toml

# remove a dependency needed only for the vendored package
sed -ri '/target_os="linux"/,/openssl/d' aw-sync/Cargo.toml

# jemallocator will not be packaged for Fedora, so remove it
sed -ri '/target_os="linux", target_arch="x86"/,+1d' aw-server/Cargo.toml
sed -ri '/target_os = "linux", target_arch = "x86"/,/static ALLOC: jemallocator::Jemalloc = jemallocator::Jemalloc;/d' aw-server/src/main.rs

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# no UI built without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_build
%cargo_license
%cargo_license_summary

%install
install -Dm 0755 %{_builddir}/%{name}-%{commit}/target/rpm/{aw-server,aw-sync} -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/aw-server -o %{buildroot}%{_mandir}/man1/aw-server.1
help2man %{buildroot}%{_bindir}/aw-sync -o %{buildroot}%{_mandir}/man1/aw-sync.1
install -Dm 0644 aw-server.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# tests report an error with EmbeddedAssets without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_test
%endif

%package     -n aw-sync
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description -n aw-sync
%{summary}

%files       -n aw-sync
%doc README.md
%license LICENSE
%{_mandir}/man1/aw-sync.1*
%{_bindir}/aw-sync

%files
%doc README.md
%license LICENSE
%{_mandir}/man1/aw-server.1*
%{_bindir}/aw-server
%{_userunitdir}/aw-server.service

%changelog
%autochangelog
