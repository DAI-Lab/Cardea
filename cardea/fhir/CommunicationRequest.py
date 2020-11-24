from .fhirbase import fhirbase


class CommunicationRequest(fhirbase):
    """
    A request to convey information; e.g. the CDS system proposes that an
    alert be sent to a responsible provider, the CDS system proposes that
    the public health agency be notified about a reportable condition.

    Args:
        resourceType: This is a CommunicationRequest resource
        identifier: A unique ID of this request for reference purposes. It
            must be provided if user wants it returned as part of any output,
            otherwise it will be autogenerated, if needed, by CDS system. Does not
            need to be the actual ID of the source system.
        basedOn: A plan or proposal that is fulfilled in whole or in part by
            this request.
        replaces: Completed or terminated request(s) whose function is taken
            by this new request.
        groupIdentifier: A shared identifier common to all requests that were
            authorized more or less simultaneously by a single author,
            representing the identifier of the requisition, prescription or
            similar form.
        status: The status of the proposal or order.
        category: The type of message to be sent such as alert, notification,
            reminder, instruction, etc.
        priority: Characterizes how quickly the proposed act must be
            initiated. Includes concepts such as stat, urgent, routine.
        medium: A channel that was used for this communication (e.g. email,
            fax).
        subject: The patient or group that is the focus of this communication
            request.
        recipient: The entity (e.g. person, organization, clinical information
            system, device, group, or care team) which is the intended target of
            the communication.
        topic: The resources which were related to producing this
            communication request.
        context: The encounter or episode of care within which the
            communication request was created.
        payload: Text, attachment(s), or resource(s) to be communicated to the
            recipient.
        occurrenceDateTime: The time when this communication is to occur.
        occurrencePeriod: The time when this communication is to occur.
        authoredOn: For draft requests, indicates the date of initial
            creation.  For requests with other statuses, indicates the date of
            activation.
        sender: The entity (e.g. person, organization, clinical information
            system, or device) which is to be the source of the communication.
        requester: The individual who initiated the request and has
            responsibility for its activation.
        reasonCode: Describes why the request is being made in coded or
            textual form.
        reasonReference: Indicates another resource whose existence justifies
            this request.
        note: Comments made about the request by the requester, sender,
            recipient, subject or other participants.
    """

    __name__ = 'CommunicationRequest'

    def __init__(self, dict_values=None):
        self.resourceType = 'CommunicationRequest'
        # type: str
        # possible values: CommunicationRequest

        self.basedOn = None
        # type: list
        # reference to Reference: identifier

        self.replaces = None
        # type: list
        # reference to Reference: identifier

        self.groupIdentifier = None
        # reference to Identifier

        self.status = None
        # type: str

        self.category = None
        # type: list
        # reference to CodeableConcept

        self.priority = None
        # type: str

        self.medium = None
        # type: list
        # reference to CodeableConcept

        self.subject = None
        # reference to Reference: identifier

        self.recipient = None
        # type: list
        # reference to Reference: identifier

        self.topic = None
        # type: list
        # reference to Reference: identifier

        self.context = None
        # reference to Reference: identifier

        self.payload = None
        # type: list
        # reference to CommunicationRequest_Payload

        self.occurrenceDateTime = None
        # type: str

        self.occurrencePeriod = None
        # reference to Period

        self.authoredOn = None
        # type: str

        self.sender = None
        # reference to Reference: identifier

        self.requester = None
        # reference to CommunicationRequest_Requester

        self.reasonCode = None
        # type: list
        # reference to CodeableConcept

        self.reasonReference = None
        # type: list
        # reference to Reference: identifier

        self.note = None
        # type: list
        # reference to Annotation

        self.identifier = None
        # type: list
        # reference to Identifier

        if dict_values:
            self.set_attributes(dict_values)
            self.assert_type()

    def get_relationships(self):

        return [
            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'medium'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'basedOn'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'subject'},

            {'parent_entity': 'CommunicationRequest_Requester',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'requester'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'identifier'},

            {'parent_entity': 'Period',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'occurrencePeriod'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'topic'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'context'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'category'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'replaces'},

            {'parent_entity': 'CommunicationRequest_Payload',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'payload'},

            {'parent_entity': 'Identifier',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'groupIdentifier'},

            {'parent_entity': 'CodeableConcept',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'reasonCode'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'sender'},

            {'parent_entity': 'Annotation',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'note'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'reasonReference'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest',
             'child_variable': 'recipient'},
        ]


class CommunicationRequest_Payload(fhirbase):
    """
    A request to convey information; e.g. the CDS system proposes that an
    alert be sent to a responsible provider, the CDS system proposes that
    the public health agency be notified about a reportable condition.

    Args:
        contentString: The communicated content (or for multi-part
            communications, one portion of the communication).
        contentAttachment: The communicated content (or for multi-part
            communications, one portion of the communication).
        contentReference: The communicated content (or for multi-part
            communications, one portion of the communication).
    """

    __name__ = 'CommunicationRequest_Payload'

    def __init__(self, dict_values=None):
        self.contentString = None
        # type: str

        self.contentAttachment = None
        # reference to Attachment

        self.contentReference = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest_Payload',
             'child_variable': 'contentReference'},

            {'parent_entity': 'Attachment',
             'parent_variable': 'object_id',
             'child_entity': 'CommunicationRequest_Payload',
             'child_variable': 'contentAttachment'},
        ]


class CommunicationRequest_Requester(fhirbase):
    """
    A request to convey information; e.g. the CDS system proposes that an
    alert be sent to a responsible provider, the CDS system proposes that
    the public health agency be notified about a reportable condition.

    Args:
        agent: The device, practitioner, etc. who initiated the request.
        onBehalfOf: The organization the device or practitioner was acting on
            behalf of.
    """

    __name__ = 'CommunicationRequest_Requester'

    def __init__(self, dict_values=None):
        self.agent = None
        # reference to Reference: identifier

        self.onBehalfOf = None
        # reference to Reference: identifier

        self.object_id = None
        # unique identifier for object class

        if dict_values:
            self.set_attributes(dict_values)

    def get_relationships(self):

        return [
            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest_Requester',
             'child_variable': 'agent'},

            {'parent_entity': 'Reference',
             'parent_variable': 'identifier',
             'child_entity': 'CommunicationRequest_Requester',
             'child_variable': 'onBehalfOf'},
        ]
