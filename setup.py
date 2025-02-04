# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import setuptools

setuptools.setup(
    name="adcm_client",
    version="2019.10.31.17",
    author="Anton Chevychalov",
    author_email="cab@arenadata.io",
    description="ArenaData Cluster Manager Client",
    url="https://github.com/arenadata/adcm",
    packages=setuptools.find_packages(),
    install_requires=['pyyaml', 'coreapi', 'ipython', 'gitpython', 'docker', 'jinja2'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/adcm_sdk_shell', 'bin/adcm_sdk_pack'],
)
