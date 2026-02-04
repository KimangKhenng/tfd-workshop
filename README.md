<div align="center">
  <img src="assets/tfd_logo.jpeg" alt="TFD Logo" width="50"/>
</div>

# TFD Workshop

[![Workshop Series](https://img.shields.io/badge/TFD-Workshop%20Series-blue.svg)](https://github.com/tfdevs/container-security-workshop-series)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Required-2496ED?logo=docker)](https://www.docker.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> **Teaching for Development (TFDvs)** - Empowering developers through hands-on, practical workshops across security, DevOps, and modern development practices.

---

## What is TFD Workshop?

**TFD Workshop** is a comprehensive educational initiative offering multiple workshop series covering essential topics in modern software development. Each series consists of progressive, hands-on sessions designed to build practical skills through real-world scenarios, live demonstrations, and interactive exercises.

### Current & Upcoming Workshop Series

#### **Web Security Series** - *IN PROGRESS*
Master security in web applications and containerized environments

- **Container Security** (7 workshops) - Currently running
  - Workshop 1: Container Security Basics ✅ Completed (Feb 4, 2026) | [Materials](./series/web-security/w1-container-security-basics/materials/workshop-1-content.md) | [Recording](#)
  - Workshops 2-7: Coming soon
- **API Security** (5 workshops) - 🚧 Coming soon
- **Authentication & Authorization** (4 workshops) - 🚧 Coming soon
- **Web Application Firewall** (3 workshops) - 🚧 Coming soon

#### **DevOps Series** - 🔜 Coming Soon
CI/CD, Infrastructure as Code, and automation

#### **Software Architecture Series** - 🔜 Coming Soon
Microservices, scalability, and design patterns

---

## Why Container Security?

Container security is critical in modern DevOps, yet many developers and engineers lack proper knowledge of security best practices. This 7-part workshop series bridges that gap with:

- **Practical, hands-on learning** - Real commands, real scenarios
- **Progressive curriculum** - From basics to advanced topics
- **Live demonstrations** - See security issues in action
- **Industry best practices** - Production-ready knowledge
- **Free and open-source** - All materials available to the community

---

## Container Security Workshops Overview

### Workshop 1: Container Security Basics ✅ COMPLETED
**Date:** February 4, 2026 | **Duration:** 2.5 hours | **Participants:** 300+

**What We Covered:**
- Containers vs VMs (Security Perspective)
- Shared Kernel Risks & Implications
- Container Isolation Boundaries
- Common Security Myths Debunked
- Hands-on Security Demonstrations

**Status:** Materials available in [`/w1-container-security-basics`](./w1-container-security-basics/)

**Recording:** [Watch on YouTube](#) | [Download Materials](./w1-container-security-basics/)

---

### Workshop 2: Image Security & Attack Surface
**Status:** 🚧 Coming Soon

**Topics:**
- How vulnerable images happen
- The `latest` tag problem
- Alpine vs Ubuntu vs Distroless
- CVE scanning & vulnerability detection
- Building minimal secure images

**Duration:** 1 hour | **Level:** Beginner

---

### Workshop 3: Runtime Security & Privileged Containers
**Status:** 🚧 Coming Soon

**Topics:**
- Linux capabilities explained
- Why `--privileged` is dangerous
- Container escape scenarios
- Running containers as non-root
- Capability dropping

**Duration:** 1-1.5 hours | **Level:** Intermediate

---

### Workshop 4: Secrets & Configuration Security
**Status:** 🚧 Coming Soon

**Topics:**
- Why secrets in images are dangerous
- Environment variables vs mounted secrets
- Docker secrets & Kubernetes secrets
- Secret rotation strategies
- Avoiding Git leaks

**Duration:** 1 hour | **Level:** Intermediate

---

### Workshop 5: Network & Access Control
**Status:** 🚧 Coming Soon

**Topics:**
- Container networking security
- Exposed ports & attack surface
- Network isolation patterns
- Service mesh basics
- Zero-trust networking

**Duration:** 1 hour | **Level:** Intermediate

---

### Workshop 6: Supply Chain & CI/CD Risks
**Status:** 🚧 Coming Soon

**Topics:**
- Image poisoning attacks
- Dependency vulnerabilities
- Tag immutability
- Container signing & verification
- CI/CD security best practices

**Duration:** 1 hour | **Level:** Advanced

---

### Workshop 7: Final Project - Secure the Broken App
**Status:** 🚧 Coming Soon

**Format:** Hands-on Security Challenge

**Scenario:** Fix a deliberately insecure containerized application

**Tasks:**
- Harden vulnerable Dockerfiles
- Remove excessive privileges
- Implement proper secret management
- Configure network isolation
- Apply defense-in-depth

**Duration:** 1-1.5 hours | **Level:** All levels

---

## 🚀 Getting Started

### Prerequisites

- **Docker** installed and running
- **Basic Linux command line** knowledge
- **Terminal** access
- **Text editor** (VS Code, Vim, etc.)
- **Internet connection** for pulling images

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tfdevs/container-security-workshop-series.git
   cd container-security-workshop-series
   ```

2. **Choose a workshop:**
   ```bash
   cd w1-container-security-basics
   ```

3. **Review the README:**
   ```bash
   cat README.md
   ```

4. **Run the setup script:**
   ```bash
   chmod +x scripts/lab-setup.sh
   ./scripts/lab-setup.sh
   ```

5. **Follow the exercises:**
   ```bash
   cat exercises/hands-on-lab.md
   ```

### Verify Your Environment

```bash
# Check Docker version
docker --version

# Test Docker is working
docker run --rm hello-world

# Check sudo access (optional but helpful)
sudo -v
```

---

## Who Should Use This?

This workshop series is perfect for:

- ✅ **Developers** using Docker in projects
- ✅ **DevOps Engineers** managing containerized workloads
- ✅ **Security Professionals** learning container security
- ✅ **CS Students** studying cloud technologies
- ✅ **System Administrators** migrating to containers
- ✅ **Tech Leads** implementing DevSecOps

---

## 📖 Learning Path

### Beginner Track
1. Workshop 1: Container Security Basics
2. Workshop 2: Image Security
3. Workshop 4: Secrets Management

### Intermediate Track
1. Workshop 3: Runtime Security
2. Workshop 5: Network Security
3. Workshop 6: Supply Chain

### Advanced Track
1. Complete Workshops 1-6
2. Workshop 7: Final Project
3. Apply in real-world scenarios

---

## 🛠️ Tools & Technologies Covered

- **Docker** - Container runtime
- **Linux** - Namespaces, cgroups, capabilities
- **Security Tools** - Trivy, Docker Bench, Falco
- **Best Practices** - CIS Benchmarks, NIST guidelines
- **Kubernetes** - Security concepts (where applicable)

---

## 📊 Workshop Statistics

### First Workshop Success 🎉
**Container Security Basics - February 4, 2026**

- **Registrations:** 300+ participants
- **Countries:** 15+ countries represented
- **Satisfaction:** 98% would recommend
- **Completion Rate:** 85% completed hands-on labs
- **Platform:** Google Meet

*This is just the beginning! More workshops and series coming soon.*

---

## TFD Mission

**"Making technology education accessible, practical, and impactful for developers worldwide."**

We believe in:
- 🎓 **Hands-on learning** over pure theory
- 🌍 **Open access** to quality education
- 💡 **Practical skills** for real-world problems
- 🤝 **Community-driven** content and collaboration
- 🚀 **Continuous learning** across all tech domains

Through TFD Workshop, we empower developers and engineers across security, DevOps, cloud, mobile, and architecture - helping you build better, more secure software.

We welcome contributions! Whether it's:

- 🐛 **Bug reports** - Found an issue? Let us know
- 💡 **Feature requests** - Have an idea? Share it
- 📝 **Documentation** - Improve our docs
- 🔧 **Code** - Submit a PR with improvements
- 🎓 **Teaching** - Share your expertise

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use these materials for personal learning
- ✅ Use them in your own workshops (with attribution)
- ✅ Modify and adapt the content
- ✅ Share with your team or community

---

## 🌟 Support & Community

### Get Help
- 📧 **Email:** contact@tfdevs.com
- 💬 **Discord:** [Join our community](#)
- 🐦 **Twitter:** [@tfdevs](https://twitter.com/tfdevs)
- 💼 **LinkedIn:** [TFDevs](https://linkedin.com/company/tfdevs)

### Stay Updated
- 🔔 **Watch** this repo for updates
- ⭐ **Star** if you find it helpful
- 🔄 **Fork** to create your own version
- 📢 **Share** with your network

---

## 📚 Additional Resources

### Official Documentation
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)
- [NIST Container Security Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-190.pdf)
- [Kubernetes Security](https://kubernetes.io/docs/concepts/security/)

### Recommended Reading
- [Container Security by Liz Rice](https://www.oreilly.com/library/view/container-security/9781492056690/)
- [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Kubernetes Security Best Practices](https://kubernetes-security.info/)

### Security Tools
- [Trivy](https://github.com/aquasecurity/trivy) - Vulnerability scanner
- [Docker Bench Security](https://github.com/docker/docker-bench-security) - Security audit
- [Falco](https://falco.org/) - Runtime security
- [Anchore](https://anchore.com/) - Container analysis

---

## 🙏 Acknowledgments

Special thanks to:
- All **300+ participants** of Workshop 1
- **Contributors** who helped improve the materials
- **Open source community** for tools and resources
- **Docker & Kubernetes** communities for documentation

---

## 📅 Upcoming Workshops & Series

Stay tuned for announcements:

### Container Security (Web Security Series)
- **Workshop 2:** Image Security (TBA)
- **Workshop 3:** Runtime Security (TBA)
- **Workshop 4:** Secrets Management (TBA)
- **Workshop 5-7:** Coming soon

### Future Series
- 🔐 **API Security Series** - RESTful API security, GraphQL security
- 🔑 **Authentication Series** - OAuth, JWT, SSO, MFA
- 🔧 **DevOps Series** - CI/CD security, IaC best practices

Follow us on social media for updates! 📢

---

## 🎯 Our Mission

**"Making technology education accessible, practical, and impactful for developers worldwide."**

---

## 📞 Contact

**TFDevs - Teaching for Development**

- 🌐 Website: [tfdevs.com](https://tfdevs.com)
- 📧 Email: info@tfdevs.com
- 🎥 YouTube: [@tfdevs](https://youtube.com/@tfdevs)
- 📘 Facebook: [TFDevs](https://facebook.com/teachingfordevelopment)

---

<div align="center">

**⭐ Star this repo to stay updated on new workshops and series!**

**🔔 Watch for announcements across all TFD Workshop series**

**🤝 Contribute to help developers worldwide learn and grow**

[⬆ Back to Top](#tfd-workshop-)

</div>
