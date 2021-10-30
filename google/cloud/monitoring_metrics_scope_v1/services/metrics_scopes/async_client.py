# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

OptionalRetry = Union[retries.Retry, object]

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.monitoring_metrics_scope_v1.types import metrics_scope
from google.cloud.monitoring_metrics_scope_v1.types import metrics_scopes
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from .transports.base import MetricsScopesTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import MetricsScopesGrpcAsyncIOTransport
from .client import MetricsScopesClient


class MetricsScopesAsyncClient:
    """Manages Cloud Monitoring Metrics Scopes, and the monitoring
    of Google Cloud projects and AWS accounts.
    """

    _client: MetricsScopesClient

    DEFAULT_ENDPOINT = MetricsScopesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = MetricsScopesClient.DEFAULT_MTLS_ENDPOINT

    metrics_scope_path = staticmethod(MetricsScopesClient.metrics_scope_path)
    parse_metrics_scope_path = staticmethod(
        MetricsScopesClient.parse_metrics_scope_path
    )
    monitored_project_path = staticmethod(MetricsScopesClient.monitored_project_path)
    parse_monitored_project_path = staticmethod(
        MetricsScopesClient.parse_monitored_project_path
    )
    common_billing_account_path = staticmethod(
        MetricsScopesClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        MetricsScopesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(MetricsScopesClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        MetricsScopesClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        MetricsScopesClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        MetricsScopesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(MetricsScopesClient.common_project_path)
    parse_common_project_path = staticmethod(
        MetricsScopesClient.parse_common_project_path
    )
    common_location_path = staticmethod(MetricsScopesClient.common_location_path)
    parse_common_location_path = staticmethod(
        MetricsScopesClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            MetricsScopesAsyncClient: The constructed client.
        """
        return MetricsScopesClient.from_service_account_info.__func__(MetricsScopesAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            MetricsScopesAsyncClient: The constructed client.
        """
        return MetricsScopesClient.from_service_account_file.__func__(MetricsScopesAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> MetricsScopesTransport:
        """Returns the transport used by the client instance.

        Returns:
            MetricsScopesTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(MetricsScopesClient).get_transport_class, type(MetricsScopesClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, MetricsScopesTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the metrics scopes client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.MetricsScopesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = MetricsScopesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_metrics_scope(
        self,
        request: Union[metrics_scopes.GetMetricsScopeRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> metrics_scope.MetricsScope:
        r"""Returns a specific ``Metrics Scope``.

        Args:
            request (Union[google.cloud.monitoring_metrics_scope_v1.types.GetMetricsScopeRequest, dict]):
                The request object. Request for the `GetMetricsScope`
                method.
            name (:class:`str`):
                Required. The resource name of the ``Metrics Scope``.
                Example:
                ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.monitoring_metrics_scope_v1.types.MetricsScope:
                Represents a [Metrics
                   Scope](\ https://cloud.google.com/monitoring/settings#concept-scope)
                   in Cloud Monitoring, which specifies one or more
                   Google projects and zero or more AWS accounts to
                   monitor together.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metrics_scopes.GetMetricsScopeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_metrics_scope,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_metrics_scopes_by_monitored_project(
        self,
        request: Union[
            metrics_scopes.ListMetricsScopesByMonitoredProjectRequest, dict
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> metrics_scopes.ListMetricsScopesByMonitoredProjectResponse:
        r"""Returns a list of every ``Metrics Scope`` that a specific
        ``MonitoredProject`` has been added to. The metrics scope
        representing the specified monitored project will always be the
        first entry in the response.

        Args:
            request (Union[google.cloud.monitoring_metrics_scope_v1.types.ListMetricsScopesByMonitoredProjectRequest, dict]):
                The request object. Request for the
                `ListMetricsScopesByMonitoredProject` method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.monitoring_metrics_scope_v1.types.ListMetricsScopesByMonitoredProjectResponse:
                Response for the ListMetricsScopesByMonitoredProject
                method.

        """
        # Create or coerce a protobuf request object.
        request = metrics_scopes.ListMetricsScopesByMonitoredProjectRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_metrics_scopes_by_monitored_project,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def create_monitored_project(
        self,
        request: Union[metrics_scopes.CreateMonitoredProjectRequest, dict] = None,
        *,
        parent: str = None,
        monitored_project: metrics_scope.MonitoredProject = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Adds a ``MonitoredProject`` with the given project ID to the
        specified ``Metrics Scope``.

        Args:
            request (Union[google.cloud.monitoring_metrics_scope_v1.types.CreateMonitoredProjectRequest, dict]):
                The request object. Request for the
                `CreateMonitoredProject` method.
            parent (:class:`str`):
                Required. The resource name of the existing
                ``Metrics Scope`` that will monitor this project.
                Example:
                ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            monitored_project (:class:`google.cloud.monitoring_metrics_scope_v1.types.MonitoredProject`):
                Required. The initial ``MonitoredProject``
                configuration. Specify only the
                ``monitored_project.name`` field. All other fields are
                ignored. The ``monitored_project.name`` must be in the
                format:
                ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}``

                This corresponds to the ``monitored_project`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.monitoring_metrics_scope_v1.types.MonitoredProject` A [project being
                   monitored](\ https://cloud.google.com/monitoring/settings/multiple-projects#create-multi)
                   by a Metrics Scope.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, monitored_project])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metrics_scopes.CreateMonitoredProjectRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if monitored_project is not None:
            request.monitored_project = monitored_project

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_monitored_project,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            metrics_scope.MonitoredProject,
            metadata_type=metrics_scopes.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def delete_monitored_project(
        self,
        request: Union[metrics_scopes.DeleteMonitoredProjectRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a ``MonitoredProject`` from the specified
        ``Metrics Scope``.

        Args:
            request (Union[google.cloud.monitoring_metrics_scope_v1.types.DeleteMonitoredProjectRequest, dict]):
                The request object. Request for the
                `DeleteMonitoredProject` method.
            name (:class:`str`):
                Required. The resource name of the ``MonitoredProject``.
                Example:
                ``locations/global/metricsScopes/{SCOPING_PROJECT_ID_OR_NUMBER}/projects/{MONITORED_PROJECT_ID_OR_NUMBER}``

                Authorization requires the following `Google
                IAM <https://cloud.google.com/iam>`__ permissions on
                both the ``Metrics Scope`` and on the
                ``MonitoredProject``: ``monitoring.metricsScopes.link``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = metrics_scopes.DeleteMonitoredProjectRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_monitored_project,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=metrics_scopes.OperationMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-monitoring-metrics-scope",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("MetricsScopesAsyncClient",)
